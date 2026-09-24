"""Slack: four comma-separated custom theme colors."""


def filename(slug):
    return f"{slug}.txt"


def emit(slug, p):
    # System navigation, selected items, presence indication, notifications.
    roles = ('slack_navigation', 'slack_selection', 'green', 'red')
    return ','.join(p[role] for role in roles) + '\n'
