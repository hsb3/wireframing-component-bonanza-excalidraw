#!/usr/bin/env python3
"""
Validate Excalidraw library files before submission.
Checks JSON structure, component count, and file integrity.
"""
import json
from pathlib import Path


def validate_excalidraw_library(file_path):
    """Validate an .excalidrawlib file."""
    print(f"\n🔍 Validating {file_path.name}...")

    try:
        # Read and parse JSON
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Check required fields
        if not isinstance(data, dict):
            print(f"  ❌ Invalid format: root should be an object")
            return False

        if 'libraryItems' not in data:
            print(f"  ❌ Missing 'libraryItems' field")
            return False

        items = data['libraryItems']
        if not isinstance(items, list):
            print(f"  ❌ 'libraryItems' should be an array")
            return False

        # Count items
        item_count = len(items)
        print(f"  ✓ Library contains {item_count} items")

        # Validate each item
        for i, item in enumerate(items):
            if 'id' not in item:
                print(f"  ⚠️  Item {i} missing 'id'")
            if 'status' not in item:
                print(f"  ⚠️  Item {i} missing 'status'")
            if 'elements' not in item:
                print(f"  ❌ Item {i} missing 'elements'")
                return False

        # Check version
        version = data.get('version', 1)
        print(f"  ✓ Library version: {version}")

        # File size check
        file_size_kb = file_path.stat().st_size / 1024
        print(f"  ✓ File size: {file_size_kb:.1f} KB")

        if file_size_kb > 2000:
            print(f"  ⚠️  Large file (>2MB) - consider splitting")

        print(f"  ✅ {file_path.name} is valid!")
        return True

    except json.JSONDecodeError as e:
        print(f"  ❌ Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    """Validate all library files."""
    print("=" * 60)
    print("EXCALIDRAW LIBRARY VALIDATION")
    print("=" * 60)

    submission_dir = Path("submission")

    # Find all .excalidrawlib files
    library_files = list(submission_dir.glob("*.excalidrawlib"))

    if not library_files:
        print("\n❌ No .excalidrawlib files found in submission/")
        return False

    print(f"\nFound {len(library_files)} library files\n")

    # Validate each file
    all_valid = True
    for lib_file in sorted(library_files):
        if not validate_excalidraw_library(lib_file):
            all_valid = False

    # Check for preview images
    print("\n" + "=" * 60)
    print("PREVIEW IMAGE CHECK")
    print("=" * 60)

    for lib_file in sorted(library_files):
        base_name = lib_file.stem
        png_file = submission_dir / f"{base_name}.png"

        if png_file.exists():
            size_kb = png_file.stat().st_size / 1024
            print(f"  ✓ {png_file.name} ({size_kb:.1f} KB)")
        else:
            print(f"  ❌ Missing: {base_name}.png")
            all_valid = False

    # Summary
    print("\n" + "=" * 60)
    if all_valid:
        print("✅ ALL VALIDATION CHECKS PASSED!")
        print("\nReady for submission to Excalidraw community.")
    else:
        print("❌ VALIDATION FAILED")
        print("\nPlease fix the issues above before submitting.")

    print("=" * 60)

    return all_valid


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
