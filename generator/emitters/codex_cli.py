"""Codex CLI: TextMate syntax themes consumed by the /theme picker."""
import plistlib


def filename(slug):
    return f"{slug}.tmTheme"


def emit(slug, p):
    settings = [{'settings': {
        'background': p['base'], 'foreground': p['text'],
        'caret': p['text'], 'selection': p['overlay'],
        'lineHighlight': p['surface'],
    }}]
    for name, scope, role in (
        ('Comments', 'comment, punctuation.definition.comment', 'subtle'),
        ('Strings', 'string', 'green'),
        ('Escapes', 'constant.character.escape', 'cyan'),
        ('Constants', 'constant.numeric, constant.language, constant.other', 'orange'),
        ('Keywords', 'keyword, storage', 'magenta'),
        ('Operators', 'keyword.operator', 'cyan'),
        ('Functions', 'entity.name.function, support.function', 'blue'),
        ('Types', 'entity.name.type, entity.name.class, support.type, support.class', 'yellow'),
        ('Variables', 'variable', 'text'),
        ('Parameters', 'variable.parameter', 'orange'),
        ('Tags', 'entity.name.tag', 'red'),
        ('Attributes', 'entity.other.attribute-name', 'yellow'),
        ('Punctuation', 'punctuation', 'subtle'),
        ('Headings', 'markup.heading, entity.name.section', 'blue'),
        ('Links', 'markup.underline.link', 'cyan'),
        ('Inline code', 'markup.raw', 'green'),
        ('Inserted', 'markup.inserted', 'green'),
        ('Deleted', 'markup.deleted', 'red'),
        ('Changed', 'markup.changed', 'yellow'),
        ('Invalid', 'invalid', 'red'),
    ):
        settings.append({'name': name, 'scope': scope,
                         'settings': {'foreground': p[role]}})
    for name, scope, style in (
        ('Bold', 'markup.bold', 'bold'),
        ('Italic', 'markup.italic', 'italic'),
    ):
        settings.append({'name': name, 'scope': scope,
                         'settings': {'fontStyle': style}})
    return plistlib.dumps({'name': slug, 'settings': settings},
                         sort_keys=False).decode()
