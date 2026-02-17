#!/usr/bin/env python3
"""
Excalidraw Wireframe Library Generator
Generates .excalidrawlib and .excalidraw preview files
"""

import argparse
from pathlib import Path
from excalidraw_gen.builder.generate import main as generate_main
from excalidraw_gen.core.themes import list_themes

def cli():
    parser = argparse.ArgumentParser(
        description="Generate Excalidraw wireframe component library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Available themes: {', '.join(list_themes())}

Examples:
  python -m excalidraw_gen                        # Mork theme (default)
  python -m excalidraw_gen --theme abc123-dark    # Dark mode theme
  python -m excalidraw_gen --theme bronzer -c 4   # Bronzer theme, 4 columns
  uv run excalidraw-generate --theme mork         # Using uv (recommended)
        """
    )
    parser.add_argument(
        '--theme',
        '-t',
        default='mork',
        choices=list_themes(),
        help='Theme to use (default: mork)'
    )
    parser.add_argument(
        '--output',
        '-o',
        default='output/mork-wireframe-kit.excalidrawlib',
        help='Output filename for library (default: output/mork-wireframe-kit.excalidrawlib)'
    )
    parser.add_argument(
        '--preview',
        '-p',
        default='output/mork-wireframe-kit-preview.excalidraw',
        help='Output filename for preview (default: output/mork-wireframe-kit-preview.excalidraw)'
    )
    parser.add_argument(
        '--no-preview',
        action='store_true',
        help='Skip generating preview document'
    )
    parser.add_argument(
        '--columns',
        '-c',
        type=int,
        default=3,
        help='Number of columns in preview grid (default: 3)'
    )
    parser.add_argument(
        '--spacing',
        '-s',
        type=int,
        default=60,
        help='Spacing between items in preview (default: 60)'
    )

    args = parser.parse_args()

    print("🎨 Excalidraw Wireframe Library Generator")
    print("=" * 50)

    generate_main(
        theme_name=args.theme,
        output_file=args.output,
        preview_file=args.preview,
        generate_preview=not args.no_preview,
        columns=args.columns,
        spacing=args.spacing
    )

if __name__ == "__main__":
    cli()
