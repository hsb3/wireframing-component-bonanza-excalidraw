"""
Library validation utilities.
Verify that generated libraries match theme specifications.
"""
import json
from pathlib import Path
from typing import Dict, List, Tuple


class LibraryValidator:
    """Validate Excalidraw library files against theme specs"""

    def __init__(self, library_path: str):
        self.library_path = Path(library_path)
        with open(self.library_path) as f:
            self.data = json.load(f)
        self.library_items = self.data.get('libraryItems', [])

    def validate_roundness(self, expected_type: int = None) -> Dict:
        """
        Validate roundness across all rectangles.

        Args:
            expected_type: Expected roundness type (1=boxy, 3=rounded, None=null)

        Returns:
            Dict with validation results
        """
        results = {
            'total_rectangles': 0,
            'null_roundness': 0,
            'by_type': {},
            'violations': []
        }

        for item in self.library_items:
            item_name = item['name']
            for el in item['elements']:
                if el['type'] == 'rectangle':
                    results['total_rectangles'] += 1
                    roundness = el.get('roundness')

                    if roundness is None:
                        results['null_roundness'] += 1
                        if expected_type is not None and expected_type != 'null':
                            results['violations'].append(f"{item_name}: null (expected type {expected_type})")
                    else:
                        rtype = roundness.get('type', 'unknown')
                        results['by_type'][rtype] = results['by_type'].get(rtype, 0) + 1
                        if expected_type == 'null' and rtype != 20:  # Allow switch (type 20)
                            results['violations'].append(f"{item_name}: type {rtype} (expected null)")
                        elif expected_type is not None and expected_type != 'null' and rtype != expected_type and rtype != 20:
                            results['violations'].append(f"{item_name}: type {rtype} (expected {expected_type})")

        return results

    def validate_colors(self, theme_class) -> Dict:
        """Validate that colors match theme specifications"""
        results = {
            'elements_checked': 0,
            'using_theme_colors': 0,
            'violations': []
        }

        theme_colors = {
            theme_class.PRIMARY,
            theme_class.SECONDARY,
            theme_class.BACKGROUND,
            theme_class.FOREGROUND,
            theme_class.BORDER,
            theme_class.SUCCESS,
            theme_class.INFO,
            theme_class.WARNING,
            theme_class.DESTRUCTIVE,
            theme_class.MUTED,
            theme_class.GRAY_50,
            theme_class.GRAY_100,
            theme_class.GRAY_300,
            theme_class.GRAY_700,
        }

        for item in self.library_items:
            for el in item['elements']:
                results['elements_checked'] += 1
                bg = el.get('backgroundColor')
                stroke = el.get('strokeColor')

                if bg and bg != 'transparent':
                    if bg in theme_colors or bg.startswith(tuple(theme_colors)):
                        results['using_theme_colors'] += 1

                if stroke and stroke != 'transparent':
                    if stroke in theme_colors or stroke.startswith(tuple(theme_colors)):
                        results['using_theme_colors'] += 1

        return results

    def validate_roughness(self, expected_roughness: int) -> Dict:
        """Validate roughness values"""
        results = {
            'total_elements': 0,
            'by_roughness': {},
            'violations': []
        }

        for item in self.library_items:
            for el in item['elements']:
                if 'roughness' in el:
                    results['total_elements'] += 1
                    rough = el['roughness']
                    results['by_roughness'][rough] = results['by_roughness'].get(rough, 0) + 1

                    if rough != expected_roughness:
                        results['violations'].append(f"{item['name']}: roughness {rough} (expected {expected_roughness})")

        return results

    def get_component_json(self, component_name: str) -> Dict:
        """Get full JSON for a specific component"""
        for item in self.library_items:
            if component_name.lower() in item['name'].lower():
                return item
        return None

    def print_report(self, theme_name: str = None):
        """Print a comprehensive validation report"""
        print(f"\n{'='*60}")
        print(f"VALIDATION REPORT: {self.library_path.name}")
        if theme_name:
            print(f"Theme: {theme_name}")
        print(f"{'='*60}\n")

        print(f"📊 Library Stats:")
        print(f"  Total components: {len(self.library_items)}")

        # Roundness
        roundness = self.validate_roundness()
        print(f"\n🔲 Roundness:")
        print(f"  Total rectangles: {roundness['total_rectangles']}")
        print(f"  Null roundness: {roundness['null_roundness']}")
        for rtype, count in sorted(roundness['by_type'].items()):
            print(f"  Type {rtype}: {count}")

        # Element type distribution
        el_types = {}
        for item in self.library_items:
            for el in item['elements']:
                etype = el['type']
                el_types[etype] = el_types.get(etype, 0) + 1

        print(f"\n📝 Element Types:")
        for etype, count in sorted(el_types.items(), key=lambda x: -x[1]):
            print(f"  {etype}: {count}")

        print(f"\n{'='*60}\n")


def validate_all_themes():
    """Validate all generated themes"""
    from excalidraw_gen.core.themes import get_theme

    themes = {
        'default': {'roundness': 3, 'roughness': 1},
        'carbon': {'roundness': 'null', 'roughness': 0},
        'warm': {'roundness': 3, 'roughness': 2},
    }

    for theme_name, specs in themes.items():
        lib_path = f"output/{theme_name}.excalidrawlib"
        if not Path(lib_path).exists():
            print(f"⚠️  {lib_path} not found, skipping...")
            continue

        validator = LibraryValidator(lib_path)
        validator.print_report(theme_name)

        # Validate roundness
        if specs['roundness'] == 'null':
            roundness_result = validator.validate_roundness(expected_type='null')
            if roundness_result['violations']:
                print(f"❌ Roundness violations found:")
                for v in roundness_result['violations'][:5]:
                    print(f"   {v}")

        # Validate roughness
        theme_class = get_theme(theme_name)
        rough_result = validator.validate_roughness(theme_class.ROUGHNESS)
        if rough_result['violations']:
            print(f"❌ Roughness violations: {len(rough_result['violations'])}")
        else:
            print(f"✅ Roughness correct: all elements use roughness={theme_class.ROUGHNESS}")


if __name__ == "__main__":
    validate_all_themes()
