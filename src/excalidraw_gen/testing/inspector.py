"""
Component inspector utility.
Pretty-print component JSON for debugging.
"""
import json
import sys
from pathlib import Path


def inspect_component(library_path: str, search_term: str):
    """
    Find and pretty-print a component's JSON.

    Args:
        library_path: Path to .excalidrawlib file
        search_term: Component name to search for (case-insensitive)
    """
    with open(library_path) as f:
        data = json.load(f)

    matches = []
    for item in data['libraryItems']:
        if search_term.lower() in item['name'].lower():
            matches.append(item)

    if not matches:
        print(f"No components found matching '{search_term}'")
        return

    if len(matches) > 1:
        print(f"Found {len(matches)} matches:")
        for i, item in enumerate(matches, 1):
            print(f"  {i}. {item['name']}")
        print()

    # Show first match
    item = matches[0]
    print(f"\n{'='*60}")
    print(f"Component: {item['name']}")
    print(f"{'='*60}\n")

    print(f"Elements: {len(item['elements'])}")
    for i, el in enumerate(item['elements'], 1):
        print(f"\n--- Element {i}: {el['type']} ---")

        # Show key properties
        if el['type'] == 'rectangle':
            print(f"  Size: {el['width']} x {el['height']}")
            print(f"  Position: ({el['x']}, {el['y']})")
            print(f"  roundness: {el.get('roundness')}")
            print(f"  roughness: {el.get('roughness')}")
            print(f"  backgroundColor: {el.get('backgroundColor')}")
            print(f"  strokeColor: {el.get('strokeColor')}")
        elif el['type'] == 'text':
            print(f"  text: {el.get('text', '')[:50]}...")
            print(f"  fontSize: {el.get('fontSize')}")
            print(f"  fontFamily: {el.get('fontFamily')}")
        elif el['type'] == 'ellipse':
            print(f"  Size: {el['width']} x {el['height']}")
            print(f"  Position: ({el['x']}, {el['y']})")


def compare_component_across_themes(component_name: str):
    """Compare a component across all three themes"""
    themes = ['default', 'carbon', 'warm']

    print(f"\n{'='*60}")
    print(f"Comparing '{component_name}' across themes")
    print(f"{'='*60}\n")

    for theme in themes:
        lib_path = f"output/{theme}.excalidrawlib"
        if not Path(lib_path).exists():
            print(f"⚠️  {theme}: file not found")
            continue

        with open(lib_path) as f:
            data = json.load(f)

        # Find component
        for item in data['libraryItems']:
            if component_name.lower() in item['name'].lower():
                print(f"--- {theme.upper()} ---")
                # Show first rectangle's key props
                for el in item['elements']:
                    if el['type'] == 'rectangle':
                        print(f"  roundness: {el.get('roundness')}")
                        print(f"  roughness: {el.get('roughness')}")
                        print(f"  backgroundColor: {el.get('backgroundColor')}")
                        break
                print()
                break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m excalidraw_gen.testing.inspector <component_name>")
        print("  python -m excalidraw_gen.testing.inspector Desktop")
        print("  python -m excalidraw_gen.testing.inspector Button")
        sys.exit(1)

    component = sys.argv[1]

    # Try default library first
    lib = "output/default.excalidrawlib"
    if Path(lib).exists():
        inspect_component(lib, component)

    # Compare across themes
    print("\n" + "="*60)
    compare_component_across_themes(component)
