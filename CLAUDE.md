# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project generates an Excalidraw component library for wireframing SaaS and AI applications. It outputs two files:
- `.excalidrawlib` - A library file that users can import into Excalidraw
- `.excalidraw` - A preview document showing all components organized in a grid

The library uses a grayscale, hand-drawn "sketchy" style optimized for low-fidelity mockups.

## Core Commands

### Generate Library
```bash
python main.py
```
Generates both the library file and preview document:
- `shadcn-saas-kit.excalidrawlib` (737KB) - 154 components
- `shadcn-saas-kit-preview.excalidraw` (841KB) - Visual preview

### CLI Options
```bash
python main.py --help                    # Show all options
python main.py --output custom.excalidrawlib
python main.py --columns 4 --spacing 80  # Customize preview layout
python main.py --no-preview              # Skip preview generation
```

## Architecture

### Component Hierarchy (5 Levels)

The library follows a design system hierarchy aligned with `ideas.md`:

1. **Level 0** (`level0_frames.py`) - `A/Frame/*`, `A/Layout/*`
   - Device frames (Desktop, Tablet, Mobile)
   - Layout primitives (Grids, Dividers, Containers)

2. **Level 1** (`level1_primitives.py`) - `A/*`
   - Atoms: Typography, Icons, Avatars, Badges
   - Controls: Buttons, Checkboxes, Switches, Progress bars

3. **Level 2** (`level2_base_ui.py`) - `B/Form/*`
   - Inputs: Text, Number, Date, Search, Upload, OTP
   - Controls: Sliders, Color pickers, Tag inputs

4. **Level 3** (`level3_modules.py`, `level3_shells.py`, `level3_organisms.py`)
   - **Modules** (`B/*`): Cards, Nav, Tabs, Charts, Overlays, Data viz
   - **Shells** (`C/Shell/*`): App layouts (3-pane, split view, mobile nav)
   - **Organisms** (`C/Block/*`, `C/Header/*`): Page sections, CRUD blocks, dashboards

5. **Level 4** (`level4_saas.py`, `level4_templates.py`)
   - **SaaS** (`SaaS:*`): Sidebars, Data tables, Login forms, Metrics
   - **Templates** (`D/Page/*`): Full page layouts (Dashboard, Chat)

6. **Level 5** (`level5_ai.py`) - `AI:*`, `C/Block/Chat/*`
   - Chat interfaces, Message bubbles, Code artifacts, Tool cards

### Naming Conventions

Components follow a hierarchical naming scheme from `ideas.md`:

```
<Layer>/<Category>/<Component>/<Variant>

Examples:
- A/Frame/Desktop/1440x900
- B/Form/Input/Text
- C/Shell/App/3Pane
- D/Page/Dashboard
```

For legacy components not yet migrated:
```
<Category>: <Component> (<Variant>)

Examples:
- Button: Primary
- Input: Search
- SaaS: Login Form
```

### ExcalidrawBuilder API

Located in `excalidraw_builder/builder.py`. Key methods:

**Primitive Shapes:**
```python
builder.rectangle(x, y, width, height, **kwargs)
builder.ellipse(x, y, width, height, **kwargs)
builder.line(x, y, points, **kwargs)  # points = [[x1,y1], [x2,y2], ...]
builder.text(x, y, content, **kwargs)
```

**Adding to Library:**
```python
builder.add_item(name, elements)  # name = component name, elements = list of shapes
```

**Common kwargs:**
- `backgroundColor`, `strokeColor` - Use `Theme.*` constants
- `fillStyle` - `"solid"` or `"hachure"`
- `strokeStyle` - `"solid"` or `"dashed"`
- `roundness` - `{"type": 3}` for rectangles, `{"type": 2}` for lines
- `opacity` - 0-100
- `fontSize` - For text elements
- `fontFamily` - `Theme.FONT_FAMILY` (hand-drawn) or `Theme.FONT_CODE` (monospace)
- `extra` - Dict for additional properties like `{"fontWeight": "bold"}`

**Theme Constants** (`excalidraw_builder/theme.py`):
```python
Theme.PRIMARY         # Black (#000000)
Theme.SECONDARY       # Light gray (#f4f4f5)
Theme.MUTED_FG        # Medium gray (#71717a)
Theme.DESTRUCTIVE     # Red (#ef4444)
Theme.BORDER          # Border gray (#e4e4e7)
Theme.INPUT           # Input border (#e4e4e7)

Theme.BTN_HEIGHT      # 40px
Theme.INPUT_WIDTH     # 250px
```

**Saving:**
```python
builder.save(filename)                    # Generates .excalidrawlib
builder.save_preview(filename, columns=3) # Generates .excalidraw preview
```

## Adding New Components

1. **Choose the right level file** based on component complexity (see hierarchy above)

2. **Add component function:**
```python
# In components/level2_base_ui.py
def add_base_ui(b):
    # ... existing components ...

    b.add_item("B/Form/Input/Phone", [
        b.text(0, 0, "Phone Number", fontSize=14, extra={"fontWeight": "bold"}),
        b.rectangle(0, 25, 250, 40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
        b.text(10, 35, "+1 (555) 123-4567", fontSize=16, strokeColor=Theme.MUTED_FG)
    ])
```

3. **Ensure function is called in `generate.py`** (usually already wired up via `__init__.py`)

4. **Run generation** to test:
```bash
python generate.py
```

5. **Verify in preview**: Open `shadcn-saas-kit-preview.excalidraw` in Excalidraw

## Key Implementation Details

### Coordinate System
- Origin (0,0) is top-left
- All positions are absolute within each library item
- When composing complex components, position elements relative to (0,0)

### Element Bounds Calculation
For proper layout in preview document, calculate component bounds:
```python
min_x = min(el["x"] for el in elements)
max_x = max(el["x"] + el.get("width", 0) for el in elements)
# Similar for y coordinates
```

### Text Sizing
The builder automatically calculates text dimensions using `estimate_text_dimensions()`:
```python
# Automatic sizing (recommended - accounts for font size and family):
b.text(x, y, "Hello World", fontSize=24, fontFamily=Theme.FONT_FAMILY)

# Manual override when needed:
b.text(x, y, "content", width=200, height=50)

# The estimation accounts for:
# - Font size (larger fonts = wider boxes)
# - Font family (Virgil/hand-drawn is wider than Helvetica)
# - Multi-line text (splits on \n)
# - Padding (4px default)
```

**Font-specific width multipliers:**
- Virgil (hand-drawn, font=1): 0.65 × fontSize per character
- Helvetica (sans-serif, font=2): 0.55 × fontSize per character
- Cascadia (monospace, font=3): 0.6 × fontSize per character

### Line/Arrow Points
Points are relative to the line's x,y position:
```python
# Horizontal line from (100, 200) to (300, 200):
b.line(100, 200, [[0, 0], [200, 0]])

# Diagonal line:
b.line(0, 0, [[0, 0], [100, 100]])
```

### Grouping
Elements in a library item are automatically grouped. Don't manually set `groupIds`.

## File Organization

```
shadcn-excalidraw/
├── main.py                  # CLI entry point - USE THIS
├── pyproject.toml           # Project config & dependencies
├── README.md
├── CLAUDE.md
└── src/
    ├── core/
    │   ├── __init__.py
    │   └── theme.py         # Foundational theme with semantic tokens
    ├── builder/
    │   ├── __init__.py
    │   ├── builder.py       # ExcalidrawBuilder class
    │   └── generate.py      # Generation logic
    └── components/          # 9 component modules
        ├── __init__.py
        ├── level0_frames.py
        ├── level1_primitives.py
        ├── level2_base_ui.py
        ├── level3_modules.py
        ├── level3_shells.py
        ├── level3_organisms.py
        ├── level4_saas.py
        ├── level4_templates.py
        └── level5_ai.py

Generated files:
├── shadcn-saas-kit.excalidrawlib          # Import into Excalidraw
└── shadcn-saas-kit-preview.excalidraw     # Visual preview document
```

## Theme Architecture

**Location:** `src/core/theme.py` (foundational - imported by builder and all components)

**Key Principle:** All colors and styling must use theme constants. No hardcoded hex colors in components.

**Semantic Token Categories:**
- **Core grayscale:** PRIMARY, SECONDARY, MUTED, BORDER, etc.
- **Success (green):** SUCCESS, SUCCESS_BG, SUCCESS_BORDER, SUCCESS_TEXT
- **Info (blue):** INFO, INFO_BG, INFO_BORDER, INFO_TEXT
- **Warning (yellow):** WARNING, WARNING_BG, WARNING_BORDER
- **Destructive (red):** DESTRUCTIVE, DESTRUCTIVE_BG, DESTRUCTIVE_BORDER

This allows cascading theme changes across all 154 components by editing one file.

## Design Philosophy

Per `ideas.md`:
- **Greyscale only** - No colors except for destructive actions (red)
- **Hand-drawn style** - Virgil font, sketchy lines (roughness=1)
- **Imply spacing** - Use 8px/16px/24px/32px increments
- **Cap variants** - 2-3 per component (default + error/loading states)
- **Searchable names** - Use path-like prefixes so library search works

## Common Patterns

### Form Field with Label
```python
b.add_item("B/Form/Input/Example", [
    b.text(0, 0, "Label", fontSize=14, extra={"fontWeight": "bold"}),
    b.rectangle(0, 25, 250, 40, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.INPUT),
    b.text(10, 35, "Placeholder text", fontSize=16, strokeColor=Theme.MUTED_FG)
])
```

### Card with Header and Content
```python
b.add_item("B/Card/Example", [
    b.rectangle(0, 0, 300, 200, backgroundColor=Theme.BACKGROUND, strokeColor=Theme.BORDER),
    b.text(20, 20, "Card Title", fontSize=18, extra={"fontWeight": "bold"}),
    b.line(0, 50, [[0, 0], [300, 0]], strokeColor=Theme.BORDER),  # Divider
    b.text(20, 70, "Card content goes here", fontSize=14)
])
```

### State Variations
```python
# Default state
b.add_item("A/Button/Primary", [...])

# Loading state
b.add_item("A/Button/Primary/Loading", [
    b.rectangle(0, 0, 120, 40, backgroundColor=Theme.PRIMARY, opacity=80),
    b.ellipse(50, 10, 20, 20, strokeStyle="dashed")  # Spinner
])
```
