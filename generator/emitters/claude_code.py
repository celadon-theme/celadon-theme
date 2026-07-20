"""Claude Code: theme JSON for ~/.claude/themes/, one <slug>.json per theme.

Role mapping mirrors the rest of the family: brand ("claude") = green, focus
chrome (prompt border, permissions, suggestions) = magenta like the
oh-my-posh caret, semantic accents honest (success green, error red, warning
yellow), diff and memory backgrounds from the generator's derived tints.
Shimmer keys use the br_* tier — brighter on dark, stronger on light. The
eight subagent labels and seven rainbow stops are a best-effort spread over
twelve accents.
"""
import json


def filename(slug):
    return f"{slug}.json"


def emit(slug, p):
    o = {
        'claude': p['green'], 'claudeShimmer': p['br_green'],
        'text': p['text'], 'inverseText': p['base'],
        'inactive': p['subtle'], 'inactiveShimmer': p['text'],
        'subtle': p['muted'],
        'suggestion': p['magenta'],
        'permission': p['magenta'], 'permissionShimmer': p['br_magenta'],
        'remember': p['yellow'],
        'success': p['green'], 'error': p['red'],
        'warning': p['yellow'], 'warningShimmer': p['br_yellow'],
        'merged': p['magenta'],
        'promptBorder': p['magenta'], 'promptBorderShimmer': p['br_magenta'],
        'planMode': p['blue'], 'autoAccept': p['yellow'],
        'bashBorder': p['red'], 'ide': p['cyan'],
        'fastMode': p['yellow'], 'fastModeShimmer': p['br_yellow'],
        'diffAdded': p['diff_add'], 'diffAddedDimmed': p['diff_add_dim'],
        'diffAddedWord': p['diff_add_word'],
        'diffRemoved': p['diff_del'], 'diffRemovedDimmed': p['diff_del_dim'],
        'diffRemovedWord': p['diff_del_word'],
        'userMessageBackground': p['surface'],
        'userMessageBackgroundHover': p['overlay'],
        'messageActionsBackground': p['surface'],
        'bashMessageBackgroundColor': p['surface'],
        'memoryBackgroundColor': p['magenta_tint'],
        'selectionBg': p['overlay'],
        'rate_limit_fill': p['magenta'], 'rate_limit_empty': p['overlay'],
        'briefLabelYou': p['cyan'], 'briefLabelClaude': p['green'],
        'red_FOR_SUBAGENTS_ONLY': p['red'],
        'blue_FOR_SUBAGENTS_ONLY': p['blue'],
        'green_FOR_SUBAGENTS_ONLY': p['green'],
        'yellow_FOR_SUBAGENTS_ONLY': p['yellow'],
        'purple_FOR_SUBAGENTS_ONLY': p['magenta'],
        'orange_FOR_SUBAGENTS_ONLY': p['br_yellow'],
        'pink_FOR_SUBAGENTS_ONLY': p['br_magenta'],
        'cyan_FOR_SUBAGENTS_ONLY': p['cyan'],
        'rainbow_red': p['red'], 'rainbow_red_shimmer': p['br_red'],
        'rainbow_orange': p['br_red'], 'rainbow_orange_shimmer': p['br_red'],
        'rainbow_yellow': p['yellow'], 'rainbow_yellow_shimmer': p['br_yellow'],
        'rainbow_green': p['green'], 'rainbow_green_shimmer': p['br_green'],
        'rainbow_blue': p['blue'], 'rainbow_blue_shimmer': p['br_blue'],
        'rainbow_indigo': p['br_blue'], 'rainbow_indigo_shimmer': p['br_blue'],
        'rainbow_violet': p['magenta'], 'rainbow_violet_shimmer': p['br_magenta'],
    }
    doc = {'name': slug.replace('-', ' ').title(),
           'base': 'light' if slug == 'celadon-sky' else 'dark',
           'overrides': o}
    return json.dumps(doc, indent=2) + '\n'
