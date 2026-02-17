"""
Warm Tones theme.
Earthy beiges, soft browns, and warm accents.
Friendly, approachable aesthetic for consumer apps.
"""

class Theme:
    # --- Core Warm Palette ---
    PRIMARY = "#8b4513"      # Saddle Brown (warm primary)
    PRIMARY_FG = "#fefcf9"   # Warm white
    SECONDARY = "#f5f0e8"    # Warm beige (light)
    SECONDARY_FG = "#3e3022" # Dark brown
    MUTED = "#f5f0e8"        # Warm beige
    MUTED_FG = "#9b8b7e"     # Warm gray
    ACCENT = "#d2691e"       # Chocolate (warm accent)
    ACCENT_FG = "#fefcf9"
    BORDER = "#e3d5c3"       # Warm border
    INPUT = "#e3d5c3"
    RING = "#8b4513"
    BACKGROUND = "#fefcf9"   # Warm white background
    FOREGROUND = "#3e3022"   # Dark brown text

    # --- Extended Warm Grays ---
    GRAY_50 = "#f9f6f1"      # Very light warm
    GRAY_100 = "#ebe3d7"     # Light warm beige
    GRAY_300 = "#c9b9a5"     # Medium warm gray
    GRAY_700 = "#5c4e3f"     # Dark warm brown

    # --- Semantic Colors: Success (Warm Green) ---
    SUCCESS = "#6b8e23"          # Olive green
    SUCCESS_FG = "#fefcf9"
    SUCCESS_BG = "#e8f3dc"       # Light olive
    SUCCESS_BORDER = "#9caf88"
    SUCCESS_TEXT = "#4a6216"     # Dark olive
    SUCCESS_BRIGHT = "#8fbc3f"   # Bright olive

    # --- Semantic Colors: Info (Warm Blue) ---
    INFO = "#5b7c99"             # Slate blue (warm tint)
    INFO_FG = "#fefcf9"
    INFO_BG = "#e8ecf1"          # Light slate
    INFO_BORDER = "#9fb3c8"
    INFO_TEXT = "#3d5266"        # Dark slate
    INFO_SUBTLE_BG = "#f2f5f8"

    # --- Semantic Colors: Warning (Amber) ---
    WARNING = "#d97706"          # Amber-600
    WARNING_FG = "#fefcf9"
    WARNING_BG = "#fef3c7"       # Amber-100
    WARNING_BORDER = "#fbbf24"   # Amber-400

    # --- Semantic Colors: Destructive (Warm Red) ---
    DESTRUCTIVE = "#b91c1c"      # Red-700
    DESTRUCTIVE_FG = "#fefcf9"
    DESTRUCTIVE_BG = "#fee2e2"   # Red-100
    DESTRUCTIVE_BORDER = "#f87171"  # Red-400

    # --- Example/Demo Colors ---
    DEMO_BLUE = "#5b7c99"        # Warm slate blue

    # --- Fonts ---
    FONT_FAMILY = 1  # Virgil for friendly hand-drawn feel
    FONT_CODE = 3

    # --- Excalidraw Specifics ---
    STROKE_STYLE = "solid"
    STROKE_WIDTH = 1
    ROUGHNESS = 2  # More sketchy/organic for warm feel

    # --- Sizing ---
    BTN_HEIGHT = 40
    BTN_WIDTH = 120
    INPUT_WIDTH = 250
    ROUNDNESS_TYPE = 3  # Rounded corners
