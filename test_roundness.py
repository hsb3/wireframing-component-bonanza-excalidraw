#!/usr/bin/env python3
"""Test roundness theme application"""
import sys
sys.path.insert(0, 'src')

from excalidraw_gen.core.themes import get_theme
from excalidraw_gen.builder import ExcalidrawBuilder

# Test with carbon theme (type 1 - boxy)
print("Testing Carbon theme (ROUNDNESS_TYPE = 1)...")
carbon = get_theme('carbon')
print(f"  Carbon ROUNDNESS_TYPE: {carbon.ROUNDNESS_TYPE}")

builder = ExcalidrawBuilder(theme=carbon)

# Create a rectangle without explicit roundness
rect1 = builder.rectangle(0, 0, 100, 100, backgroundColor="#ff0000")
print(f"  Rectangle (no override): roundness = {rect1.get('roundness')}")

# Create a rectangle WITH explicit roundness
rect2 = builder.rectangle(0, 0, 100, 100, roundness={"type": 10})
print(f"  Rectangle (explicit type 10): roundness = {rect2.get('roundness')}")

# Test with default theme (type 3 - rounded)
print("\nTesting Default theme (ROUNDNESS_TYPE = 3)...")
default = get_theme('default')
print(f"  Default ROUNDNESS_TYPE: {default.ROUNDNESS_TYPE}")

builder2 = ExcalidrawBuilder(theme=default)
rect3 = builder2.rectangle(0, 0, 100, 100)
print(f"  Rectangle (no override): roundness = {rect3.get('roundness')}")

print("\n✅ Test complete!")
