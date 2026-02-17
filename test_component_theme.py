#!/usr/bin/env python3
"""Test that components see the correct theme"""
import sys
sys.path.insert(0, 'src')

# Simulate what generate.py does
from excalidraw_gen.core.themes import get_theme
import types

# Load carbon theme
carbon = get_theme('carbon')
print(f"Selected theme: carbon")
print(f"ROUNDNESS_TYPE: {carbon.ROUNDNESS_TYPE}")
print(f"FONT_FAMILY: {carbon.FONT_FAMILY}")
print(f"ROUGHNESS: {carbon.ROUGHNESS}")

# Inject into sys.modules
theme_module = types.ModuleType('theme')
theme_module.Theme = carbon
sys.modules['theme'] = theme_module
sys.modules['excalidraw_gen.core.themes.default'] = theme_module

# Now import a component and test
from excalidraw_gen.components.level1_primitives import add_primitives
from excalidraw_gen.builder import ExcalidrawBuilder

# Import Theme as components do
from excalidraw_gen.core.themes.default import Theme
print(f"\nImported Theme attributes:")
print(f"  ROUNDNESS_TYPE: {Theme.ROUNDNESS_TYPE}")
print(f"  FONT_FAMILY: {Theme.FONT_FAMILY}")
print(f"  PRIMARY: {Theme.PRIMARY}")

# Create builder and add primitives
builder = ExcalidrawBuilder(theme=carbon)
add_primitives(builder)

# Check a few created elements
print(f"\nChecking generated elements:")
for item in builder.library_items[:3]:
    name = item['name']
    elements = item['elements']
    for el in elements[:2]:  # Check first 2 elements
        if el['type'] == 'rectangle':
            roundness = el.get('roundness', 'None')
            print(f"  {name}: rectangle roundness = {roundness}")
            break

print("\n✅ Component theme test complete!")
