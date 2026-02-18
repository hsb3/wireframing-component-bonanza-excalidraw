#!/usr/bin/env python3
"""
Generate component-registry.json from .excalidrawlib files
Provides metadata for AI agent to understand available components
"""
import json
from pathlib import Path
import sys

def extract_component_metadata(library_file: Path) -> list[dict]:
    """Extract component metadata from .excalidrawlib file"""
    with open(library_file) as f:
        library = json.load(f)

    components = []
    theme_name = library_file.stem.replace('-wireframe-kit', '')

    for idx, item in enumerate(library.get('libraryItems', [])):
        name = item.get('name', f'Component-{idx}')
        elements = item.get('elements', [])

        if not elements:
            continue

        # Calculate bounding box
        xs = [el.get('x', 0) for el in elements if 'x' in el]
        ys = [el.get('y', 0) for el in elements if 'y' in el]
        widths = [el.get('x', 0) + el.get('width', 0) for el in elements if 'width' in el]
        heights = [el.get('y', 0) + el.get('height', 0) for el in elements if 'height' in el]

        min_x = min(xs) if xs else 0
        min_y = min(ys) if ys else 0
        max_x = max(widths) if widths else 100
        max_y = max(heights) if heights else 100

        width = int(max_x - min_x)
        height = int(max_y - min_y)

        # Extract text elements for customization
        text_fields = [
            el.get('text', '')
            for el in elements
            if el.get('type') == 'text' and el.get('text')
        ]

        # Generate tags from component name
        tags = generate_tags(name)

        # Parse category hierarchy
        category_info = parse_component_name(name)

        component = {
            'id': f"{theme_name}-{idx}",
            'name': name,
            'theme': theme_name,
            'category': category_info.get('category', 'Uncategorized'),
            'subcategory': category_info.get('subcategory', ''),
            'description': generate_description(name, elements),
            'dimensions': {
                'width': width,
                'height': height
            },
            'element_count': len(elements),
            'text_fields': text_fields,
            'tags': tags,
            'library_file': str(library_file.relative_to(library_file.parent.parent)),
            'library_index': idx
        }

        components.append(component)

    return components

def generate_tags(name: str) -> list[str]:
    """Generate searchable tags from component name"""
    tags = []
    name_lower = name.lower()

    # Extract words from name
    words = name.replace('/', ' ').replace(':', ' ').replace('(', ' ').replace(')', ' ').split()
    tags.extend([w.lower() for w in words if len(w) > 2])

    # Common categories
    tag_map = {
        'button': ['button', 'action', 'cta'],
        'input': ['input', 'form', 'field'],
        'card': ['card', 'container', 'panel'],
        'table': ['table', 'data', 'grid'],
        'chart': ['chart', 'graph', 'visualization'],
        'nav': ['navigation', 'menu', 'navbar'],
        'sidebar': ['sidebar', 'nav', 'menu'],
        'header': ['header', 'top', 'navbar'],
        'login': ['login', 'auth', 'signin'],
        'dashboard': ['dashboard', 'overview', 'home'],
        'chat': ['chat', 'message', 'conversation'],
    }

    for keyword, related_tags in tag_map.items():
        if keyword in name_lower:
            tags.extend(related_tags)

    return list(set(tags))

def parse_component_name(name: str) -> dict:
    """Parse hierarchical component name (A/Frame/Desktop or Button: Primary)"""
    if '/' in name:
        parts = name.split('/')
        return {
            'level': parts[0] if len(parts) > 0 else '',
            'category': parts[1] if len(parts) > 1 else '',
            'subcategory': parts[2] if len(parts) > 2 else '',
            'variant': parts[3] if len(parts) > 3 else ''
        }
    elif ':' in name:
        parts = name.split(':')
        return {
            'category': parts[0].strip(),
            'variant': parts[1].strip() if len(parts) > 1 else ''
        }
    else:
        return {'category': name}

def generate_description(name: str, elements: list) -> str:
    """Generate human-readable description"""
    element_types = [el.get('type') for el in elements]
    type_counts = {
        'rectangle': element_types.count('rectangle'),
        'ellipse': element_types.count('ellipse'),
        'text': element_types.count('text'),
        'line': element_types.count('line'),
        'arrow': element_types.count('arrow')
    }

    # Simple description based on name
    desc_map = {
        'button': 'Interactive button component',
        'input': 'Text input field',
        'card': 'Container card component',
        'table': 'Data table component',
        'chart': 'Chart visualization',
        'login': 'Login form component',
        'dashboard': 'Dashboard layout',
        'frame': 'Device frame container',
    }

    name_lower = name.lower()
    for keyword, desc in desc_map.items():
        if keyword in name_lower:
            return desc

    return f"Component with {len(elements)} elements"

def main():
    """Generate component registry from all .excalidrawlib files"""

    # Find library files
    project_root = Path(__file__).parent.parent.parent.parent
    library_path = project_root / 'output'

    if not library_path.exists():
        print(f"Error: Library path not found: {library_path}")
        sys.exit(1)

    library_files = list(library_path.glob('*.excalidrawlib'))

    if not library_files:
        print(f"Error: No .excalidrawlib files found in {library_path}")
        sys.exit(1)

    print(f"Found {len(library_files)} library files:")
    for lib in library_files:
        print(f"  - {lib.name}")

    # Extract metadata from all libraries
    all_components = []
    for lib_file in library_files:
        print(f"\nProcessing {lib_file.name}...")
        components = extract_component_metadata(lib_file)
        all_components.extend(components)
        print(f"  Extracted {len(components)} components")

    # Build registry
    registry = {
        'version': '1.0.0',
        'total_components': len(all_components),
        'themes': list(set(c['theme'] for c in all_components)),
        'categories': list(set(c['category'] for c in all_components)),
        'components': all_components
    }

    # Save to backend data directory
    output_dir = Path(__file__).parent.parent / 'src' / 'data'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'component-registry.json'

    with open(output_file, 'w') as f:
        json.dump(registry, f, indent=2)

    print(f"\n✅ Component registry saved to: {output_file}")
    print(f"   Total components: {registry['total_components']}")
    print(f"   Themes: {', '.join(registry['themes'])}")
    print(f"   Categories: {len(registry['categories'])}")

    # Also create a human-readable catalog
    catalog_file = output_dir / 'component-catalog.txt'
    with open(catalog_file, 'w') as f:
        f.write("# Wireframe Component Catalog\n\n")

        for theme in registry['themes']:
            theme_comps = [c for c in all_components if c['theme'] == theme]
            f.write(f"## Theme: {theme.upper()} ({len(theme_comps)} components)\n\n")

            # Group by category
            categories = {}
            for comp in theme_comps:
                cat = comp['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(comp)

            for cat, comps in sorted(categories.items()):
                f.write(f"### {cat} ({len(comps)})\n")
                for comp in comps[:10]:  # First 10 per category
                    f.write(f"- {comp['name']} - {comp['description']} ({comp['dimensions']['width']}×{comp['dimensions']['height']}px)\n")
                if len(comps) > 10:
                    f.write(f"  ... and {len(comps) - 10} more\n")
                f.write("\n")

    print(f"✅ Human-readable catalog saved to: {catalog_file}")

if __name__ == '__main__':
    main()
