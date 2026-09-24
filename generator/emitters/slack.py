"""Slack: ten comma-separated legacy theme colors, ready for Import theme.

Modern Slack maps imported colors to its built-in palette. These slots
describe the legacy format, not ten independently configurable modern colors.
"""


def filename(slug):
    return f"{slug}.txt"


def emit(slug, p):
    roles = (
        'base',     # column background
        'surface',  # menu background
        'magenta',  # active item
        'base',     # active item text
        'overlay',  # hover item
        'text',     # text color
        'green',    # active presence
        'red',      # mention badge
        'surface',  # top navigation background
        'text',     # top navigation text
    )
    return ','.join(p[role] for role in roles) + '\n'
