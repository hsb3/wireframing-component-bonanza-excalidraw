#!/usr/bin/env python3
"""
Create high-quality showcase files with best components in mosaic layout.
"""
import json
from pathlib import Path

THEMES = {
    "default": {
        "library": "submission/shadcn-wireframe-default.excalidrawlib",
        "output": "showcase-default.excalidraw",
        "bg_color": "#ffffff"
    },
    "carbon": {
        "library": "submission/shadcn-wireframe-carbon.excalidrawlib",
        "output": "showcase-carbon.excalidraw",
        "bg_color": "#161616"
    },
    "warm": {
        "library": "submission/shadcn-wireframe-warm.excalidrawlib",
        "output": "showcase-warm.excalidraw",
        "bg_color": "#fef9f5"
    }
}

# Exact component names to showcase (handpicked for impact)
# Format: (name_pattern, size) where size is 'xl', 'large', 'wide', 'tall', 'medium', 'small'
SHOWCASE_COMPONENTS = [
    # Hero components (large, impressive)
    ("D/Page/Dashboard", "xl"),
    ("D/Page/Chat", "xl"),
    ("SaaS: CRUD Table", "large"),
    ("SaaS: Login Form", "wide"),

    # Feature components (medium-large)
    ("SaaS: Data Table", "wide"),
    ("AI: Chat Thread", "tall"),
    ("C/Block/CRUD/List+Table", "large"),
    ("SaaS: Chart (Bar)", "wide"),
    ("Frame: Desktop", "large"),
    ("Frame: Mobile", "tall"),

    # Module components
    ("SaaS: Navbar", "wide"),
    ("SaaS: Sidebar", "tall"),
    ("B/Card/Pricing", "medium"),
    ("B/Card/Metric", "medium"),
    ("C/Shell/Mobile/BottomNav", "medium"),
    ("B/Nav/Tabs/Line", "medium"),

    # Form & UI components (small-medium)
    ("Form: Field (Label+Input)", "medium"),
    ("Input: Search", "small"),
    ("Input: Select", "small"),
    ("Button: Primary", "small"),
    ("Button: Destructive", "small"),
    ("Control: Checkbox (Active)", "small"),
    ("Control: Switch", "small"),
    ("Control: Radio", "small"),

    # Data & messaging
    ("AI: Tool Call", "medium"),
    ("C/Block/Chat/MessageBubble", "medium"),
    ("B/Alert/Info", "medium"),
    ("A/Badge/Status", "small"),
    ("A/Avatar/Circle", "small"),
    ("A/Progress/Bar", "small"),
]


def find_component(items, pattern):
    """Find component by name pattern."""
    for item in items:
        name = item.get('name', '')
        if pattern.lower() in name.lower():
            return item
    return None


def select_showcase_components(library_file):
    """Select handpicked showcase components."""
    with open(library_file, 'r') as f:
        data = json.load(f)

    items = data.get('libraryItems', [])
    selected = []

    for pattern, size in SHOWCASE_COMPONENTS:
        comp = find_component(items, pattern)
        if comp:
            selected.append((comp, size))

    print(f"  Found {len(selected)}/{len(SHOWCASE_COMPONENTS)} components")
    return selected


def create_optimized_layout():
    """Create magazine-style mosaic layout."""
    # Mosaic grid: (row, col, width_cells, height_cells, size_category)
    return [
        # Row 0-1: Hero section
        (0, 0, 3, 2, "xl"),      # Dashboard or Chat App
        (0, 3, 2, 1, "wide"),    # Login form or Data table
        (0, 5, 1, 2, "tall"),    # Mobile frame or Sidebar
        (1, 3, 1, 1, "medium"),  # Card or form field
        (1, 4, 1, 1, "small"),   # Button or input

        # Row 2-3: Content section
        (2, 0, 2, 2, "large"),   # Desktop frame or CRUD table
        (2, 2, 2, 1, "wide"),    # Chart or Navbar
        (2, 4, 1, 1, "medium"),  # Metric card
        (2, 5, 1, 1, "small"),   # Badge or avatar
        (3, 2, 1, 1, "small"),   # Checkbox
        (3, 3, 1, 1, "small"),   # Switch
        (3, 4, 1, 1, "small"),   # Radio
        (3, 5, 1, 1, "small"),   # Progress

        # Row 4-5: Details section
        (4, 0, 1, 2, "tall"),    # Chat thread or Sidebar
        (4, 1, 2, 1, "wide"),    # Table or Tabs
        (4, 3, 2, 1, "medium"),  # Form field or Alert
        (4, 5, 1, 1, "small"),   # Input
        (5, 1, 1, 1, "medium"),  # Pricing card
        (5, 2, 1, 1, "medium"),  # Message bubble
        (5, 3, 1, 1, "small"),   # Button
        (5, 4, 1, 1, "small"),   # Search
        (5, 5, 1, 1, "small"),   # Avatar

        # Row 6-7: Footer section
        (6, 0, 3, 1, "wide"),    # Bottom nav or tab bar
        (6, 3, 2, 1, "medium"),  # Tool call card
        (6, 5, 1, 1, "small"),   # Badge
        (7, 0, 1, 1, "small"),   # Icon
        (7, 1, 2, 1, "medium"),  # Navigation menu
        (7, 3, 1, 1, "small"),   # Select
        (7, 4, 1, 1, "small"),   # Upload
        (7, 5, 1, 1, "small"),   # Status badge
    ]


def arrange_mosaic(components_with_sizes, layout, cell_size=250):
    """Arrange components in optimized mosaic."""
    all_elements = []
    element_id = 1000

    # Match components to layout cells by size
    size_buckets = {'xl': [], 'large': [], 'wide': [], 'tall': [], 'medium': [], 'small': []}
    for comp, size in components_with_sizes:
        size_buckets[size].append(comp)

    for row, col, w_cells, h_cells, size_cat in layout:
        # Get component from appropriate size bucket
        if size_buckets[size_cat]:
            item = size_buckets[size_cat].pop(0)
        else:
            # Fallback to any available component
            for bucket in size_buckets.values():
                if bucket:
                    item = bucket.pop(0)
                    break
            else:
                continue

        # Calculate cell position and size
        x = col * cell_size
        y = row * cell_size
        cell_w = w_cells * cell_size
        cell_h = h_cells * cell_size

        elements = item.get('elements', [])
        if not elements:
            continue

        # Get component bounds
        xs = [el.get('x', 0) for el in elements]
        ys = [el.get('y', 0) for el in elements]
        min_x, min_y = min(xs), min(ys)
        max_x = max(el.get('x', 0) + el.get('width', 0) for el in elements)
        max_y = max(el.get('y', 0) + el.get('height', 0) for el in elements)
        comp_w, comp_h = max_x - min_x, max_y - min_y

        # Scale to fit cell with minimal padding
        padding = 15
        available_w = cell_w - 2 * padding
        available_h = cell_h - 2 * padding

        if comp_w > 0 and comp_h > 0:
            scale = min(available_w / comp_w, available_h / comp_h, 2.0)
        else:
            scale = 1.0

        # Center in cell
        scaled_w = comp_w * scale
        scaled_h = comp_h * scale
        offset_x = x + (cell_w - scaled_w) / 2
        offset_y = y + (cell_h - scaled_h) / 2

        # Transform elements
        for el in elements:
            new_el = {**el}
            new_el['x'] = (el.get('x', 0) - min_x) * scale + offset_x
            new_el['y'] = (el.get('y', 0) - min_y) * scale + offset_y

            if 'width' in new_el:
                new_el['width'] = new_el['width'] * scale
            if 'height' in new_el:
                new_el['height'] = new_el['height'] * scale
            if 'fontSize' in new_el:
                new_el['fontSize'] = max(8, new_el['fontSize'] * scale)
            if 'points' in new_el:
                new_el['points'] = [[px * scale, py * scale] for px, py in new_el['points']]
            if 'strokeWidth' in new_el:
                new_el['strokeWidth'] = max(0.5, new_el['strokeWidth'] * scale)

            new_el['id'] = f"element-{element_id}"
            element_id += 1

            if 'groupIds' in new_el:
                del new_el['groupIds']

            all_elements.append(new_el)

    return all_elements


def create_showcase(theme_key, config):
    """Create optimized showcase file."""
    print(f"\n📋 {theme_key.upper()} theme:")

    components = select_showcase_components(config['library'])
    layout = create_optimized_layout()

    elements = arrange_mosaic(components, layout, cell_size=250)
    print(f"  Arranged {len(elements)} elements in mosaic")

    showcase = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": config['bg_color'],
            "gridSize": None,
            "zoom": {"value": 1}
        },
        "files": {}
    }

    with open(config['output'], 'w') as f:
        json.dump(showcase, f, indent=2)

    print(f"  ✓ Saved to {config['output']}")


def main():
    print("=" * 60)
    print("CREATING OPTIMIZED SHOWCASE FILES")
    print("=" * 60)

    for theme_key, config in THEMES.items():
        create_showcase(theme_key, config)

    print("\n" + "=" * 60)
    print("✅ SHOWCASES CREATED")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
