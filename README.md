# Excalidraw Wireframe Kit (SaaS & AI)

A hand-drawn style component library for wireframing SaaS applications and AI interfaces in Excalidraw.
Inspired by [shadcn/ui](https://ui.shadcn.com/), but optimized for low-fidelity "sketchy" mockups.

## Features
*   **154 Components**: Comprehensive library covering frames, primitives, forms, navigation, data display, and AI chat patterns
*   **5-Level Hierarchy**: Organized from basic primitives to complete page templates
*   **Hand-drawn Style**: Uses the Virgil font and sketchy lines for a true wireframe feel
*   **Preview Document**: Auto-generated visual catalog of all components
*   **SaaS Components**: Sidebars, Navbars, Data Tables, Metric Cards, CRUD layouts
*   **AI Components**: Chat interfaces, Message bubbles, Code blocks, Tool cards
*   **Grayscale Only**: Clean, distraction-free palette

## Quick Start

1.  **Generate the Library**
    ```bash
    # Using Python module
    python -m excalidraw_gen

    # Or with uv (recommended)
    uv run excalidraw-generate
    ```
    This creates in `output/`:
    - `shadcn-saas-kit.excalidrawlib` (737KB) - The component library with 154 components
    - `shadcn-saas-kit-preview.excalidraw` (841KB) - Visual preview document

2.  **Try Different Themes**
    ```bash
    python -m excalidraw_gen --theme carbon    # IBM Carbon dark theme
    python -m excalidraw_gen --theme warm      # Warm earthy tones
    python -m excalidraw_gen --theme default   # Original grayscale

    # Or with uv
    uv run excalidraw-generate --theme carbon
    ```

3.  **Import into Excalidraw**
    *   Open [Excalidraw](https://excalidraw.com)
    *   Go to **Library** → **Open**
    *   Select `output/shadcn-saas-kit.excalidrawlib`

4.  **Browse Components**
    *   Open `output/shadcn-saas-kit-preview.excalidraw` in Excalidraw to see all 154 components organized by category

## Component Hierarchy

**Level 0**: Frames & Layout (`level0_frames.py`)
- Device frames (Desktop, Tablet, Mobile)
- Layout primitives (Grids, Dividers, Scroll areas)

**Level 1**: Primitives (`level1_primitives.py`)
- Typography (H1-H3, Body, Links, Code)
- Icons and Avatars
- Basic controls (Buttons, Badges, Steppers, Progress bars)

**Level 2**: Base UI (`level2_base_ui.py`)
- Form inputs (Text, Number, Date, Search, Upload, Tags)
- Controls (Checkboxes, Radios, Switches, Sliders)
- Button variants

**Level 3**: Composite Components
- **Modules** (`level3_modules.py`): Cards, Navigation, Tabs, Charts, Overlays, Data viz
- **Shells** (`level3_shells.py`): App layouts (3-pane, split view, mobile nav)
- **Organisms** (`level3_organisms.py`): Page headers, CRUD blocks, Dashboard sections

**Level 4**: Complex Patterns
- **SaaS** (`level4_saas.py`): Sidebars, Data tables, Login forms, Metrics grids
- **Templates** (`level4_templates.py`): Full page layouts (Dashboard, Chat)

**Level 5**: AI Patterns (`level5_ai.py`)
- Chat interfaces (Thread lists, Message bubbles, Composer)
- AI-specific components (Thinking indicators, Tool cards, Code artifacts)

## Available Themes

### Default - Grayscale Wireframes

![Default Theme Preview](submission/shadcn-wireframe-default.png)

**default** - Original grayscale wireframe style
- Hand-drawn Virgil font
- Pure grayscale (black/white/gray)
- Sketchy aesthetic (roughness=1)

### Carbon - IBM Carbon Design System

![Carbon Theme Preview](submission/shadcn-wireframe-carbon.png)

**carbon** - IBM Carbon Design System inspired
- Dark mode (#161616 background)
- High contrast with blue accents (#0f62fe)
- Clean, corporate aesthetic (roughness=0)
- Cascadia monospace font

### Warm - Friendly Earth Tones

![Warm Theme Preview](submission/shadcn-wireframe-warm.png)

**warm** - Warm earthy tones
- Beiges, soft browns, warm grays
- Friendly, approachable feel
- Hand-drawn style (roughness=2)
- Warm color accents

## Project Structure

```
root/
├── pyproject.toml           # uv-compatible package config
├── output/                  # Generated libraries (gitignored)
└── src/
    └── excalidraw_gen/      # Main package
        ├── __main__.py      # python -m excalidraw_gen
        ├── cli.py           # CLI logic
        ├── core/
        │   └── themes/      # Theme definitions
        │       ├── default.py
        │       ├── carbon.py
        │       └── warm.py
        ├── builder/
        │   ├── builder.py   # ExcalidrawBuilder class
        │   └── generate.py  # Generation orchestration
        └── components/      # 9 component modules
            ├── level0_frames.py
            ├── level1_primitives.py
            ├── level2_base_ui.py
            ├── level3_modules.py
            ├── level3_shells.py
            ├── level3_organisms.py
            ├── level4_saas.py
            ├── level4_templates.py
            └── level5_ai.py
```

## Customization

### Modify Theme
Edit `src/core/theme.py` to change:
- **Semantic color tokens** (success, info, warning, destructive)
- **Grayscale palette** (primary, secondary, muted, borders)
- **Fonts** (hand-drawn vs sans-serif vs monospace)
- **Stroke styles and roughness**
- **Default sizing** (button height, input width, etc.)

All components reference theme constants, so changes cascade automatically.

### Add New Components

1. Choose the appropriate level file in `components/`
2. Add your component using the `ExcalidrawBuilder` API:

```python
def add_base_ui(b):
    # ... existing components ...

    b.add_item("B/Form/Input/Phone", [
        b.text(0, 0, "Phone Number", fontSize=14),
        b.rectangle(0, 25, 250, 40, strokeColor=Theme.INPUT),
        b.text(10, 35, "+1 (555) 000-0000", strokeColor=Theme.MUTED_FG)
    ])
```

3. Run `make generate` or `PYTHONPATH=src python -m excalidraw_gen` to rebuild

### Customize Preview Layout

Modify the preview generation in `src/builder/generate.py`:

```python
builder.save_preview(
    "preview.excalidraw",
    columns=4,      # Number of columns
    spacing=80      # Spacing between items
)
```

## Development

See [CLAUDE.md](CLAUDE.md) for detailed architecture documentation and API reference.
