# Visibility Improvements for Excalidraw Library Components

## Problem Statement

Components appear as "white blobs" on Excalidraw's default white canvas due to insufficient contrast between component backgrounds, borders, and the canvas.

## Root Causes

### 1. **Low Border Contrast**
- Original `BORDER = "#e4e4e7"` (Zinc-200)
- Contrast ratio vs white: **1.15:1** (WCAG minimum is 3:1 for UI)
- Barely visible on white canvas

### 2. **Pure White Backgrounds**
- Original `BACKGROUND = "#ffffff"`
- Invisible when placed on white Excalidraw canvas
- No differentiation between component and canvas

### 3. **Secondary Colors Too Light**
- `SECONDARY = "#f4f4f5"` (Zinc-100)
- Almost indistinguishable from white

## Changes Made

### Theme Updates (`src/excalidraw_gen/core/themes/default.py`)

```python
# BEFORE
BORDER = "#e4e4e7"       # Zinc-200 (contrast: 1.15:1)
INPUT = "#e4e4e7"        # Zinc-200
BACKGROUND = "#ffffff"   # Pure white

# AFTER
BORDER = "#d4d4d8"       # Zinc-300 (contrast: 1.5:1) ✓
INPUT = "#d4d4d8"        # Zinc-300 ✓
BACKGROUND = "#fafafa"   # Zinc-50 (subtle gray) ✓
```

### New Tokens Added

```python
GRAY_400 = "#a1a1aa"          # Zinc-400 (for strong borders)
BORDER_LIGHT = "#e4e4e7"      # Zinc-200 (subtle dividers)
BORDER_STRONG = "#a1a1aa"     # Zinc-400 (emphasized borders)
```

## Design Heuristics Applied

### 1. **Minimum Contrast Ratio**
- **Goal:** 1.5:1 minimum for borders, 3:1 for critical UI elements
- **Applied:** Increased border from Zinc-200 → Zinc-300
- **Further improvement:** Consider Zinc-400 (#a1a1aa) for input borders

### 2. **Background Differentiation**
- **Principle:** Never use pure white for component backgrounds on white canvas
- **Applied:** Changed from `#ffffff` → `#fafafa` (Zinc-50)
- **Effect:** Creates subtle depth and separation

### 3. **Progressive Enhancement Strategy**
- Light borders (`BORDER_LIGHT`) for non-interactive elements (dividers, card borders)
- Medium borders (`BORDER`) for default interactive elements (inputs, buttons)
- Strong borders (`BORDER_STRONG`) for focus/active states

### 4. **Sketchy Style Compensation**
- Excalidraw's `roughness=1` makes borders appear lighter/more diffuse
- Compensate by using borders 1-2 shades darker than typical design systems

## Recommended Next Steps

### Phase 1: Quick Wins (Component Updates)
Update high-visibility components to use new tokens:

1. **Input Fields** - Use `BORDER_STRONG` instead of `INPUT` for better visibility:
   ```python
   b.rectangle(0,0,w,h, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER_STRONG)
   ```

2. **Cards/Containers** - Keep using `BORDER` but with new Zinc-300 value

3. **Outline Buttons** - Use `BORDER_STRONG`:
   ```python
   b.rectangle(0,0,w,h, backgroundColor="transparent", strokeColor=Theme.BORDER_STRONG)
   ```

### Phase 2: Component-Specific Improvements

#### Empty States & Subtle Backgrounds
```python
# Instead of pure white circles
b.ellipse(0,0,80,80, backgroundColor=Theme.GRAY_100, fillStyle="solid")
```

#### Switch Controls
```python
# White knob needs stronger border for visibility
b.ellipse(2,2,20,20, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER, fillStyle="solid")
```

#### Secondary Buttons
Current secondary buttons use `SECONDARY = #f4f4f5` which is nearly white. Consider:
```python
# Option A: Keep light but add visible border
b.rectangle(0,0,w,h, backgroundColor=Theme.SECONDARY, strokeColor=Theme.BORDER, fillStyle="solid")

# Option B: Darken slightly to GRAY_100
b.rectangle(0,0,w,h, backgroundColor=Theme.GRAY_100, strokeColor=Theme.BORDER, fillStyle="solid")
```

### Phase 3: Create Theme Variants

For users who want even stronger visibility, create alternate themes:

1. **High Contrast Theme** (`themes/high_contrast.py`)
   - `BORDER = "#a1a1aa"` (Zinc-400)
   - `BACKGROUND = "#f4f4f5"` (Zinc-100)

2. **Paper Theme** (`themes/paper.py`)
   - `BACKGROUND = "#f5f5f4"` (Stone-100 - warmer gray)
   - Mimics paper texture for better visibility

## Validation

### Before Regenerating:
1. Check all components using `Theme.BACKGROUND`
2. Identify any with `strokeColor="transparent"` (Ghost buttons, etc.)
3. Review components with nested white elements (switches, checkboxes)

### Testing:
1. Generate library: `python main.py`
2. Import into Excalidraw on **white canvas**
3. Check visibility of:
   - Input fields (most critical)
   - Secondary buttons
   - Card borders
   - Empty states
   - Switch controls

## Impact Summary

- ✓ **Border visibility:** 30% improvement (Zinc-200 → Zinc-300)
- ✓ **Background separation:** Subtle gray prevents "white blob" effect
- ✓ **Flexibility:** New tokens (`BORDER_LIGHT`, `BORDER_STRONG`) for granular control
- ✓ **Backwards compatible:** Changes preserve design intent while fixing visibility

## References

- [WCAG Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [Tailwind Zinc Colors](https://tailwindcss.com/docs/customizing-colors) - Reference palette
- [shadcn/ui Design System](https://ui.shadcn.com/) - Inspiration for semantic tokens
