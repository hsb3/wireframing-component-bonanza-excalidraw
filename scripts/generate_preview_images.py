#!/usr/bin/env python3
"""
Generate preview images by rendering Excalidraw components using Pillow.
Creates a grid layout showing ~20-25 representative components.
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

THEMES = {
    "default": {
        "library_file": "submission/shadcn-wireframe-default.excalidrawlib",
        "output_file": "submission/shadcn-wireframe-default.png",
        "bg_color": "#ffffff"
    },
    "carbon": {
        "library_file": "submission/shadcn-wireframe-carbon.excalidrawlib",
        "output_file": "submission/shadcn-wireframe-carbon.png",
        "bg_color": "#161616"
    },
    "warm": {
        "library_file": "submission/shadcn-wireframe-warm.excalidrawlib",
        "output_file": "submission/shadcn-wireframe-warm.png",
        "bg_color": "#fef9f5"
    }
}

# Components to showcase - more comprehensive like reference image
SHOWCASE_PATTERNS = [
    "Desktop", "Mobile", "Tablet",
    "Button", "Input", "Dropdown", "Checkbox", "Switch", "Radio", "Toggle",
    "Card", "Navbar", "Tab", "Sidebar", "Breadcrumb",
    "Chart", "Table", "Progress", "Stats", "Metric",
    "Dashboard", "Login", "Settings", "Profile",
    "Chat", "Message", "Avatar", "Badge", "Icon",
    "Dialog", "Modal", "Alert", "Toast", "Notification",
    "Calendar", "Date", "Picker",
    "Form", "Search", "Upload", "Select",
    "Menu", "Nav", "Header", "Footer",
    "Data", "Grid", "List"
]


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    if hex_color == 'transparent':
        return None
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def render_element(draw, element, scale=1.0, offset_x=0, offset_y=0):
    """Render a single Excalidraw element."""
    el_type = element.get('type')
    x = int((element.get('x', 0) + offset_x) * scale)
    y = int((element.get('y', 0) + offset_y) * scale)

    stroke_color = element.get('strokeColor', '#000000')
    fill_color = element.get('backgroundColor', 'transparent')
    stroke_width = max(1, int(element.get('strokeWidth', 1) * scale))

    stroke_rgb = hex_to_rgb(stroke_color)
    fill_rgb = hex_to_rgb(fill_color)

    if el_type == 'rectangle':
        width = int(element.get('width', 0) * scale)
        height = int(element.get('height', 0) * scale)

        if fill_rgb:
            draw.rectangle([x, y, x + width, y + height], fill=fill_rgb)
        if stroke_rgb:
            draw.rectangle([x, y, x + width, y + height], outline=stroke_rgb, width=stroke_width)

    elif el_type == 'ellipse':
        width = int(element.get('width', 0) * scale)
        height = int(element.get('height', 0) * scale)

        if fill_rgb:
            draw.ellipse([x, y, x + width, y + height], fill=fill_rgb)
        if stroke_rgb:
            draw.ellipse([x, y, x + width, y + height], outline=stroke_rgb, width=stroke_width)

    elif el_type in ('line', 'arrow'):
        points = element.get('points', [[0, 0]])
        coords = []
        for px, py in points:
            coords.extend([int((x + px) * scale), int((y + py) * scale)])

        if stroke_rgb and len(coords) >= 4:
            draw.line(coords, fill=stroke_rgb, width=stroke_width)

    elif el_type == 'text':
        text = element.get('text', '')
        font_size = max(8, int(element.get('fontSize', 16) * scale))

        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
        except:
            font = ImageFont.load_default()

        if stroke_rgb and text:
            draw.text((x, y), text, fill=stroke_rgb, font=font)


def get_element_bounds(elements):
    """Calculate bounding box of elements."""
    if not elements:
        return 0, 0, 100, 100

    xs = []
    ys = []
    for el in elements:
        x = el.get('x', 0)
        y = el.get('y', 0)
        xs.extend([x, x + el.get('width', 0)])
        ys.extend([y, y + el.get('height', 0)])

    return min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)


def select_showcase_components(library_file):
    """Select representative components."""
    with open(library_file, 'r') as f:
        data = json.load(f)

    library_items = data.get('libraryItems', [])
    selected = []

    # Try to match each pattern
    for pattern in SHOWCASE_PATTERNS:
        for item in library_items:
            name = item.get('name', '')
            if pattern.lower() in name.lower() and item not in selected:
                selected.append(item)
                break
        if len(selected) >= 48:  # 6x8 grid
            break

    # Fill up to 48 if needed
    for item in library_items:
        if item not in selected:
            selected.append(item)
        if len(selected) >= 48:
            break

    return selected[:48]


def create_preview_image(library_file, output_file, bg_color):
    """Create preview image with grid of components."""
    print(f"  Loading {Path(library_file).name}...")

    if not Path(library_file).exists():
        print(f"  ❌ File not found")
        return False

    components = select_showcase_components(library_file)
    print(f"  Selected {len(components)} components")

    # Grid configuration - show more components like reference
    columns = 6
    rows = 8
    cell_width = 200
    cell_height = 150
    padding = 12

    # Create image
    img_width = columns * cell_width
    img_height = rows * cell_height

    img = Image.new('RGB', (img_width, img_height), hex_to_rgb(bg_color))
    draw = ImageDraw.Draw(img)

    print(f"  Rendering {len(components)} components in {columns}x{rows} grid...")

    # Render each component
    for idx, item in enumerate(components[:48]):
        if idx >= columns * rows:
            break

        row = idx // columns
        col = idx % columns

        cell_x = col * cell_width
        cell_y = row * cell_height

        elements = item.get('elements', [])
        if not elements:
            continue

        # Get bounds
        min_x, min_y, width, height = get_element_bounds(elements)

        # Calculate scale to fit in cell
        max_size = min(cell_width - 2*padding, cell_height - 2*padding)
        if width > 0 and height > 0:
            scale = min(max_size / width, max_size / height, 1.5)
        else:
            scale = 1.0

        # Center in cell
        offset_x = cell_x + (cell_width - width * scale) / 2 - min_x * scale
        offset_y = cell_y + (cell_height - height * scale) / 2 - min_y * scale

        # Render each element
        for element in elements:
            render_element(draw, element, scale, offset_x / scale, offset_y / scale)

    # Save
    img.save(output_file, 'PNG', optimize=True)

    size_kb = Path(output_file).stat().st_size / 1024
    print(f"  ✓ Created {Path(output_file).name} ({size_kb:.1f} KB)")
    return True


def main():
    """Generate all preview images."""
    print("=" * 70)
    print("GENERATING PREVIEW IMAGES (Grid Layout)")
    print("=" * 70)
    print()

    Path("submission").mkdir(exist_ok=True)

    for theme_key, config in THEMES.items():
        print(f"📸 {theme_key.upper()} theme:")
        try:
            create_preview_image(
                config["library_file"],
                config["output_file"],
                config["bg_color"]
            )
        except Exception as e:
            print(f"  ❌ Error: {e}")
            import traceback
            traceback.print_exc()
        print()

    print("=" * 70)
    print("✅ COMPLETE")
    print("=" * 70)
    print()
    for theme_key, config in THEMES.items():
        output_path = Path(config["output_file"])
        if output_path.exists():
            size_kb = output_path.stat().st_size / 1024
            print(f"  ✓ {output_path.name} ({size_kb:.1f} KB)")
    print()


if __name__ == "__main__":
    main()
