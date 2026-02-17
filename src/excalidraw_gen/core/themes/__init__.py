"""
Theme loader for Excalidraw library generation.
Provides theme selection via name.
"""

from .default import Theme as DefaultTheme
from .carbon import Theme as CarbonTheme
from .warm import Theme as WarmTheme

AVAILABLE_THEMES = {
    'default': DefaultTheme,
    'carbon': CarbonTheme,
    'warm': WarmTheme,
}

def get_theme(name='default'):
    """
    Get theme by name.

    Args:
        name: Theme name ('default', 'carbon', 'warm')

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

__all__ = ['get_theme', 'list_themes', 'AVAILABLE_THEMES', 'DefaultTheme', 'CarbonTheme', 'WarmTheme']
