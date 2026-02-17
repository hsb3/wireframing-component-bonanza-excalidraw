#!/usr/bin/env python3
"""Test full generation with carbon theme"""
import sys
sys.path.insert(0, 'src')

from excalidraw_gen.builder.generate import main

# Generate with carbon theme
print("Generating with carbon theme...")
builder = main(theme_name='carbon', output_file='output/test-carbon.excalidrawlib', preview_file='output/test-carbon-preview.excalidraw', generate_preview=False)

print(f"\nChecking roundness in generated components:")
rect_roundness = {}

for item in builder.library_items:
    for el in item['elements']:
        if el['type'] == 'rectangle' and 'roundness' in el:
            roundness_type = el['roundness'].get('type')
            rect_roundness[roundness_type] = rect_roundness.get(roundness_type, 0) + 1

print(f"\nRectangle roundness distribution:")
for rtype, count in sorted(rect_roundness.items()):
    print(f"  Type {rtype}: {count} rectangles")

total = sum(rect_roundness.values())
type1_count = rect_roundness.get(1, 0)
print(f"\n📊 Summary:")
print(f"  Total rectangles with roundness: {total}")
print(f"  Type 1 (boxy): {type1_count} ({100*type1_count/total if total > 0 else 0:.1f}%)")
print(f"  Other types: {total - type1_count}")
