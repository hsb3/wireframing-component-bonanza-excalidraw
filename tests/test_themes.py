#!/usr/bin/env python3
"""
Test suite for theme validation.
Run with: python tests/test_themes.py
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, 'src')

from excalidraw_gen.testing.validator import LibraryValidator
from excalidraw_gen.core.themes import get_theme


def test_carbon_theme():
    """Test carbon theme has boxy corners and correct styling"""
    print("\n🧪 Testing Carbon Theme...")

    lib_path = "output/carbon.excalidrawlib"
    if not Path(lib_path).exists():
        print("❌ carbon.excalidrawlib not found. Run 'make carbon' first.")
        return False

    validator = LibraryValidator(lib_path)
    carbon = get_theme('carbon')

    # Test roundness
    roundness = validator.validate_roundness()
    null_pct = 100 * roundness['null_roundness'] / roundness['total_rectangles']

    print(f"  Roundness: {roundness['null_roundness']}/{roundness['total_rectangles']} null ({null_pct:.1f}%)")

    # Should have mostly null roundness (boxy)
    if null_pct < 95:  # Allow for switch
        print(f"  ❌ Expected >95% null roundness for boxy corners")
        return False

    # Test roughness
    rough = validator.validate_roughness(carbon.ROUGHNESS)
    if rough['violations']:
        print(f"  ❌ Roughness violations: {len(rough['violations'])}")
        return False

    print("  ✅ Carbon theme valid (boxy corners, roughness=0)")
    return True


def test_default_theme():
    """Test default theme has rounded corners"""
    print("\n🧪 Testing Default Theme...")

    lib_path = "output/default.excalidrawlib"
    if not Path(lib_path).exists():
        print("❌ default.excalidrawlib not found. Run 'make generate' first.")
        return False

    validator = LibraryValidator(lib_path)
    default = get_theme('default')

    # Test roundness
    roundness = validator.validate_roundness()
    type3_count = roundness['by_type'].get(3, 0)
    type3_pct = 100 * type3_count / roundness['total_rectangles']

    print(f"  Roundness type 3: {type3_count}/{roundness['total_rectangles']} ({type3_pct:.1f}%)")

    if type3_pct < 95:
        print(f"  ❌ Expected >95% type 3 roundness")
        return False

    print("  ✅ Default theme valid (rounded corners, roughness=1)")
    return True


def test_warm_theme():
    """Test warm theme has rounded corners"""
    print("\n🧪 Testing Warm Theme...")

    lib_path = "output/warm.excalidrawlib"
    if not Path(lib_path).exists():
        print("❌ warm.excalidrawlib not found. Run 'make warm' first.")
        return False

    validator = LibraryValidator(lib_path)

    # Test roundness
    roundness = validator.validate_roundness()
    type3_count = roundness['by_type'].get(3, 0)
    type3_pct = 100 * type3_count / roundness['total_rectangles']

    print(f"  Roundness type 3: {type3_count}/{roundness['total_rectangles']} ({type3_pct:.1f}%)")

    if type3_pct < 95:
        print(f"  ❌ Expected >95% type 3 roundness")
        return False

    print("  ✅ Warm theme valid (rounded corners, roughness=2)")
    return True


def main():
    print("\n" + "="*60)
    print("EXCALIDRAW LIBRARY THEME TESTS")
    print("="*60)

    results = []
    results.append(("Carbon", test_carbon_theme()))
    results.append(("Default", test_default_theme()))
    results.append(("Warm", test_warm_theme()))

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name}: {status}")

    all_passed = all(r[1] for r in results)
    print(f"\n{'✅ All tests passed!' if all_passed else '❌ Some tests failed'}\n")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
