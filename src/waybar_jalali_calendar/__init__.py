"""waybar-jalali-calendar - Jalali (Persian/Solar Hijri) calendar module for Waybar."""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("waybar-jalali-calendar")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"
