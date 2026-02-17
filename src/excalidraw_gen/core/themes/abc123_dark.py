"""
abc123-dark: Dark mode wireframe theme

⚠️  IMPORTANT: Use with Excalidraw DARK MODE canvas
This theme is designed for dark backgrounds. Components will be hard to see
on light/white canvas. In Excalidraw, toggle dark mode before using this library.

Features:
- High contrast colors for dark backgrounds
- Light borders (GRAY_40) visible on dark canvas
- Clean, professional aesthetic
- Corporate/enterprise design language
"""

class Theme:
    # --- Carbon Color Palette (Official Hex Values) ---
    # Grays
    GRAY_10 = "#f4f4f4"
    GRAY_20 = "#e0e0e0"
    GRAY_30 = "#c6c6c6"
    GRAY_40 = "#a8a8a8"
    GRAY_50 = "#8d8d8d"
    GRAY_60 = "#6f6f6f"
    GRAY_70 = "#525252"
    GRAY_80 = "#393939"
    GRAY_90 = "#262626"
    GRAY_100 = "#161616"

    # Blues
    BLUE_30 = "#a6c8ff"
    BLUE_40 = "#78a9ff"
    BLUE_50 = "#4589ff"
    BLUE_60 = "#0f62fe"
    BLUE_70 = "#0043ce"

    # Greens
    GREEN_40 = "#42be65"
    GREEN_50 = "#24a148"
    GREEN_70 = "#0e6027"

    # Reds
    RED_50 = "#fa4d56"
    RED_60 = "#da1e28"
    RED_80 = "#750e13"

    # Yellows
    YELLOW_30 = "#f1c21b"
    YELLOW_80 = "#684e00"

    # Purples
    PURPLE_40 = "#be95ff"

    # --- Core Background & Text Tokens (Gray 100 Theme) ---
    BACKGROUND = GRAY_100        # Main canvas background
    FOREGROUND = GRAY_10         # Primary text color

    # Layer tokens (surfaces/cards stacked on background)
    LAYER_01 = GRAY_90           # First level surface
    LAYER_02 = GRAY_80           # Second level surface
    LAYER_03 = GRAY_70           # Third level surface

    # Text hierarchy
    TEXT_PRIMARY = GRAY_10       # High emphasis text
    TEXT_SECONDARY = GRAY_30     # Medium emphasis text
    TEXT_PLACEHOLDER = GRAY_60   # Placeholder/hint text
    TEXT_ON_COLOR = "#ffffff"    # Text on interactive colors
    TEXT_INVERSE = GRAY_100      # Text on light backgrounds

    # --- Core Semantic Tokens (Mapped to Carbon Tokens) ---
    PRIMARY = BLUE_60            # Primary interactive color (buttons, links)
    PRIMARY_FG = "#ffffff"       # Text on primary color

    SECONDARY = GRAY_70          # Secondary surfaces (elevated from background)
    SECONDARY_FG = GRAY_10       # Text on secondary surfaces

    MUTED = GRAY_80              # Muted backgrounds (layer 1)
    MUTED_FG = GRAY_20           # Text on muted backgrounds (lighter for contrast)

    ACCENT = BLUE_60             # Accent color for highlights
    ACCENT_FG = "#ffffff"        # Text on accent color

    # --- Border Tokens ---
    # For dark theme: borders need to be MUCH lighter to show up
    BORDER = GRAY_40             # Subtle borders (high contrast on dark bg)
    BORDER_STRONG = GRAY_30      # Strong emphasis borders (very light)
    BORDER_INTERACTIVE = BLUE_50 # Interactive element borders
    BORDER_INVERSE = GRAY_10     # Borders on dark backgrounds

    # --- Input/Field Tokens ---
    INPUT = GRAY_80              # Input field background (elevated)
    RING = BLUE_50               # Focus ring color

    # --- Link Tokens ---
    LINK_PRIMARY = BLUE_40       # Primary links
    LINK_SECONDARY = BLUE_30     # Secondary links
    LINK_VISITED = PURPLE_40     # Visited link state

    # --- Semantic Colors: Success (Green) ---
    SUCCESS = GREEN_50           # Success actions/states
    SUCCESS_FG = "#ffffff"       # Text on success color
    SUCCESS_BG = GREEN_70        # Success background (dark)
    SUCCESS_BORDER = GREEN_40    # Success border
    SUCCESS_TEXT = GREEN_40      # Success text on dark bg
    SUCCESS_BRIGHT = GREEN_40    # Bright success accent

    # --- Semantic Colors: Info (Blue) ---
    INFO = BLUE_60               # Info actions/states
    INFO_FG = "#ffffff"          # Text on info color
    INFO_BG = BLUE_70            # Info background (dark)
    INFO_BORDER = BLUE_50        # Info border
    INFO_TEXT = BLUE_50          # Info text on dark bg
    INFO_SUBTLE_BG = BLUE_70     # Subtle info background

    # --- Semantic Colors: Warning (Yellow) ---
    WARNING = YELLOW_30          # Warning actions/states
    WARNING_FG = "#000000"       # Text on warning color
    WARNING_BG = YELLOW_80       # Warning background (dark)
    WARNING_BORDER = YELLOW_30   # Warning border

    # --- Semantic Colors: Destructive (Red) ---
    DESTRUCTIVE = RED_60         # Destructive actions (delete, error)
    DESTRUCTIVE_FG = "#ffffff"   # Text on destructive color
    DESTRUCTIVE_BG = RED_80      # Destructive background (dark)
    DESTRUCTIVE_BORDER = RED_60  # Destructive border

    # --- AI-Specific Tokens (Carbon v11+) ---
    AI_BORDER = BLUE_40          # AI element borders
    AI_BACKGROUND = GRAY_100     # AI popover/panel background
    CHAT_BUBBLE_USER = GRAY_80   # User message bubble
    CHAT_AVATAR_USER = BLUE_50   # User avatar background

    # --- Example/Demo Colors ---
    DEMO_BLUE = BLUE_60          # For color picker examples

    # --- Fonts ---
    # 1: Virgil (Hand-drawn), 2: Helvetica (Sans-serif), 3: Cascadia (Code)
    FONT_FAMILY = 3  # Cascadia (monospace, closest to IBM Plex Mono)
    FONT_CODE = 3    # Cascadia (IBM Plex Mono equivalent)

    # --- Excalidraw Specifics ---
    STROKE_STYLE = "solid"       # Carbon uses clean, solid strokes
    STROKE_WIDTH = 1             # Standard stroke width
    ROUGHNESS = 0                # Clean, non-sketchy for enterprise
    ROUNDNESS_TYPE = 1           # Sharp corners (boxy, no rounding)

    # --- Sizing ---
    BTN_HEIGHT = 40              # Standard button height
    BTN_WIDTH = 120              # Standard button width
    INPUT_WIDTH = 250            # Standard input width

    # --- Extended Grays (Legacy Tailwind Compatibility) ---
    # These override Carbon palette values for component compatibility
    # Mapped to Carbon grays for dark theme:
    GRAY_50 = "#525252"          # Carbon Gray-70 (subtle borders, disabled)
    GRAY_100 = "#393939"         # Carbon Gray-80 (neutral surfaces)
    GRAY_300 = "#a8a8a8"         # Carbon Gray-40 (medium borders, dividers)
    GRAY_700 = "#e0e0e0"         # Carbon Gray-20 (high contrast text/borders)
