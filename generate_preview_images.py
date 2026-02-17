#!/usr/bin/env python3
"""
Generate preview images for Excalidraw library submissions.
Creates informative preview graphics showing library contents.
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Theme configurations
THEMES = {
    "default": {
        "name": "shadcn Wireframe Kit (Default)",
        "bg_color": "#ffffff",
        "primary": "#000000",
        "secondary": "#71717a",
        "accent": "#f4f4f5",
        "description": "Hand-drawn grayscale wireframes"
    },
    "carbon": {
        "name": "shadcn Wireframe Kit (Carbon)",
        "bg_color": "#161616",
        "primary": "#f4f4f4",
        "secondary": "#c6c6c6",
        "accent": "#0f62fe",
        "description": "IBM Carbon Design System (Dark)"
    },
    "warm": {
        "name": "shadcn Wireframe Kit (Warm)",
        "bg_color": "#fef9f5",
        "primary": "#78350f",
        "secondary": "#92400e",
        "accent": "#f59e0b",
        "description": "Warm, friendly color palette"
    }
}

COMPONENT_CATEGORIES = [
    ("Frames & Layout", ["Desktop Frame", "Mobile Frame", "Tablet Frame", "Grids"]),
    ("UI Primitives", ["Buttons", "Icons", "Badges", "Avatars", "Typography"]),
    ("Form Elements", ["Inputs", "Dropdowns", "Checkboxes", "Sliders", "Upload"]),
    ("Data Display", ["Tables", "Charts", "Cards", "Stats", "Progress"]),
    ("Navigation", ["Navbar", "Tabs", "Breadcrumbs", "Pagination"]),
    ("SaaS Patterns", ["Dashboards", "Login Forms", "Settings", "Data Tables"]),
    ("AI Components", ["Chat Interface", "Message Bubbles", "Tool Cards"])
]


def create_preview_image(theme_key, output_path):
    """Create a preview image for the given theme."""
    theme = THEMES[theme_key]

    # Image dimensions
    width, height = 1200, 800

    # Create image
    img = Image.new('RGB', (width, height), theme["bg_color"])
    draw = ImageDraw.Draw(img)

    # Try to load a font, fall back to default if not available
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        header_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Draw title
    y_pos = 50
    draw.text((60, y_pos), theme["name"], fill=theme["primary"], font=title_font)
    y_pos += 60

    # Draw description
    draw.text((60, y_pos), theme["description"], fill=theme["secondary"], font=body_font)
    y_pos += 40

    # Draw component count badge
    badge_text = "154 Components"
    badge_x, badge_y = 60, y_pos
    badge_width, badge_height = 200, 40
    draw.rounded_rectangle(
        [(badge_x, badge_y), (badge_x + badge_width, badge_y + badge_height)],
        radius=8,
        fill=theme["accent"]
    )
    # Calculate text position for centering
    text_bbox = draw.textbbox((0, 0), badge_text, font=body_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = badge_x + (badge_width - text_width) // 2
    text_y = badge_y + (badge_height - text_height) // 2
    text_color = theme["bg_color"] if theme_key != "default" else theme["primary"]
    draw.text((text_x, text_y), badge_text, fill=text_color, font=body_font)
    y_pos += 80

    # Draw component categories in two columns
    draw.text((60, y_pos), "Component Categories", fill=theme["primary"], font=header_font)
    y_pos += 50

    # Left column
    col1_x = 60
    col2_x = 620
    col_y = y_pos

    for i, (category, components) in enumerate(COMPONENT_CATEGORIES):
        x_pos = col1_x if i < 4 else col2_x

        if i == 4:
            col_y = y_pos  # Reset y for second column

        # Category name
        draw.text((x_pos, col_y), f"• {category}", fill=theme["primary"], font=body_font)
        col_y += 35

        # Component items (indented)
        for comp in components[:3]:  # Show first 3
            draw.text((x_pos + 20, col_y), comp, fill=theme["secondary"], font=small_font)
            col_y += 25

        if i < 3:  # Add spacing between categories in left column
            col_y += 15
        elif i >= 4:  # Add spacing in right column
            col_y += 15

    # Draw footer
    footer_y = height - 60
    draw.text((60, footer_y), "github.com/hsb3/shadcn-excalidraw", fill=theme["secondary"], font=small_font)
    draw.text((width - 200, footer_y), "MIT License", fill=theme["secondary"], font=small_font)

    # Save image
    img.save(output_path, 'PNG', optimize=True)
    print(f"✓ Created {output_path}")


def main():
    """Generate preview images for all themes."""
    output_dir = Path("submission")
    output_dir.mkdir(exist_ok=True)

    print("Generating preview images...\n")

    for theme_key in THEMES.keys():
        output_path = output_dir / f"shadcn-wireframe-{theme_key}.png"
        create_preview_image(theme_key, output_path)

    print("\n✅ All preview images generated!")
    print(f"\nSaved to {output_dir}/")
    print("  - shadcn-wireframe-default.png")
    print("  - shadcn-wireframe-carbon.png")
    print("  - shadcn-wireframe-warm.png")


if __name__ == "__main__":
    main()
