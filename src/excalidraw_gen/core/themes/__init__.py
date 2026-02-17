"""
Theme loader for Excalidraw library generation.
Provides theme selection via name.
"""

from .mork import Theme as MorkTheme
from .abc123_dark import Theme as Abc123DarkTheme
from .bronzer import Theme as BronzerTheme

AVAILABLE_THEMES = {
    'mork': MorkTheme,
    'abc123-dark': Abc123DarkTheme,
    'bronzer': BronzerTheme,
}

def get_theme(name='mork'):
    """
    Get theme by name.

    Args:
        name: Theme name ('mork', 'abc123-dark', 'bronzer')

    Returns:
        Theme class

    Raises:
        ValueError if theme name not found
    """
    if name not in AVAILABLE_THEMES:
        available = ', '.join(AVAILABLE_THEMES.keys())
        raise ValueError(f"Unknown theme '{name}'. Available: {available}")

    return AVAILABLE_THEMES[name]

def list_themes():
    """Return list of available theme names."""
    return list(AVAILABLE_THEMES.keys())

__all__ = ['get_theme', 'list_themes', 'AVAILABLE_THEMES', 'MorkTheme', 'Abc123DarkTheme', 'BronzerTheme']
