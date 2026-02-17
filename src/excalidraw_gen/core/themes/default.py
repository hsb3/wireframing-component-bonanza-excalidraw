"""
Foundational theme configuration for the Excalidraw wireframe library.
All colors and styling constants used across components.
"""

class Theme:
    # --- Core Grayscale Palette ---
    PRIMARY = "#000000"      # Black
    PRIMARY_FG = "#ffffff"   # White
    SECONDARY = "#f4f4f5"    # Zinc-100
    SECONDARY_FG = "#18181b" # Zinc-900
    MUTED = "#f4f4f5"        # Zinc-100
    MUTED_FG = "#71717a"     # Zinc-500
    ACCENT = "#f4f4f5"       # Zinc-100
    ACCENT_FG = "#18181b"    # Zinc-900
    BORDER = "#d4d4d8"       # Zinc-300 (increased contrast from #e4e4e7)
    INPUT = "#d4d4d8"        # Zinc-300 (increased contrast from #e4e4e7)
    RING = "#000000"
    BACKGROUND = "#fafafa"   # Zinc-50 (subtle gray instead of pure white)
    FOREGROUND = "#09090b"   # Zinc-950

    # --- Extended Grays ---
    GRAY_50 = "#f8fafc"      # Slate-50 (subtle backgrounds)
    GRAY_100 = "#f3f4f6"     # Gray-100 (neutral backgrounds)
    GRAY_300 = "#d1d5db"     # Gray-300 (borders, disabled)
    GRAY_400 = "#a1a1aa"     # Zinc-400 (strong borders for emphasis)
    GRAY_700 = "#374151"     # Gray-700 (dark text)

    # --- Border Variants (for enhanced visibility) ---
    BORDER_LIGHT = "#e4e4e7"   # Zinc-200 (subtle dividers)
    BORDER_STRONG = "#a1a1aa"  # Zinc-400 (emphasized borders)

    # --- Semantic Colors: Success (Green) ---
    SUCCESS = "#16a34a"          # Green-600 (primary success)
    SUCCESS_FG = "#ffffff"       # White
    SUCCESS_BG = "#dcfce7"       # Green-100 (light background)
    SUCCESS_BORDER = "#86efac"   # Green-300 (border)
    SUCCESS_TEXT = "#166534"     # Green-800 (text on light bg)
    SUCCESS_BRIGHT = "#4ade80"   # Green-400 (bright accents)

    # --- Semantic Colors: Info (Blue) ---
    INFO = "#2563eb"             # Blue-600 (primary info/links)
    INFO_FG = "#ffffff"          # White
    INFO_BG = "#eff6ff"          # Blue-50 (light background)
    INFO_BORDER = "#bfdbfe"      # Blue-200 (border)
    INFO_TEXT = "#1e40af"        # Blue-800 (text on light bg)
    INFO_SUBTLE_BG = "#e0f2fe"   # Sky-50 (very subtle)

    # --- Semantic Colors: Warning (Yellow) ---
    WARNING = "#facc15"          # Yellow-400 (warnings)
    WARNING_FG = "#000000"       # Black
    WARNING_BG = "#fef9c3"       # Yellow-100
    WARNING_BORDER = "#fde047"   # Yellow-300

    # --- Semantic Colors: Destructive (Red) ---
    DESTRUCTIVE = "#ef4444"      # Red-500
    DESTRUCTIVE_FG = "#ffffff"   # White
    DESTRUCTIVE_BG = "#fee2e2"   # Red-100 (light background)
    DESTRUCTIVE_BORDER = "#fca5a5"  # Red-300

    # --- Example/Demo Colors ---
    DEMO_BLUE = "#3b82f6"        # Blue-500 (for color picker examples)

    # --- Fonts ---
    # 1: Virgil (Hand-drawn), 2: Helvetica (Sans-serif), 3: Cascadia (Code)
    FONT_FAMILY = 1
    FONT_CODE = 3

    # --- Excalidraw Specifics ---
    STROKE_STYLE = "solid"
    STROKE_WIDTH = 1
    ROUGHNESS = 1  # Sketchy look

    # --- Sizing ---
    BTN_HEIGHT = 40
    BTN_WIDTH = 120
    INPUT_WIDTH = 250
    ROUNDNESS_TYPE = 3  # Rounded corners
