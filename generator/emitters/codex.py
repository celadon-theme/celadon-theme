"""Codex desktop: v1 appearance share strings.

Schema verified against the desktop app's theme share parser. Code syntax
uses the built-in Codex theme; custom TextMate themes are CLI-only.
"""
import json


def filename(slug):
    return f"{slug}.txt"


def emit(slug, p):
    light = slug == 'celadon-sky'
    theme = {
        'accent': p['green'], 'accentSource': 'custom',
        'contrast': {'celadon-sky': 45, 'celadon-powder': 40,
                     'celadon': 60, 'celadon-jade': 80}[slug],
        'fonts': {'code': None, 'ui': None},
        'ink': p['text'], 'opaqueWindows': True,
        'semanticColors': {'diffAdded': p['green'], 'diffRemoved': p['red'],
                           'skill': p['magenta']},
        'surface': p['base'],
    }
    return 'codex-theme-v1:' + json.dumps({
        'codeThemeId': 'codex', 'theme': theme,
        'variant': 'light' if light else 'dark',
    }, separators=(',', ':')) + '\n'
