"""Port emitters. One module per port format; each exposes exactly:

  filename(slug) -> str   the file name this port expects for a theme
  emit(slug, palette) -> str   complete file content (palette: role → hex)

Emitters do no color math — they only format. Registering a new port is a
module plus one entry here.
"""
from . import ghostty

PORTS = {'ghostty': ghostty}
