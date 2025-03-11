#!/usr/bin/env python

"""
Constructs themes/solarized.json

Notes:
- Transparency is supported, just append to hex (e.g. `80` for 50%)
"""

import json

solarized = {
    "base03": "#002b36",  # dark background
    "base02": "#073642",  # dark background highlights
    "base01": "#586e75",  # dark comments / secondary content; light optional emphasized content
    "base00": "#657b83",  # light body text / default code / primary content
    "base0": "#839496",  # dark body text / default code / primary content
    "base1": "#93a1a1",  # dark optional emphasized content; light comments / secondary content
    "base2": "#eee8d5",  # light background highlights
    "base3": "#fdf6e3",  # light background
    "yellow": "#b58900",
    "orange": "#cb4b16",
    "red": "#dc322f",
    "magenta": "#d33682",
    "violet": "#6c71c4",
    "blue": "#268bd2",
    "cyan": "#2aa198",
    "green": "#859900",
}


def solarized_theme(solarized):
    players = [
        {
            "background": solarized[color],
            "cursor": solarized[color],
            "selection": solarized[color] + "66",
        }
        for color in [
            "blue",
            "cyan",
            "green",
            "magenta",
            "orange",
            "red",
            "violet",
            "yellow",
        ]
    ]
    syntax = {
        "attribute": {"color": solarized["blue"]},
        "boolean": {"color": solarized["yellow"]},
        "comment": {"color": solarized["fg2"], "font_style": "italic"},
        "comment.doc": {"color": solarized["fg2"], "font_style": "italic"},
        "constant": {"color": solarized["cyan"]},
        "constructor": {"color": solarized["blue"]},
        "embedded": {"color": solarized["fg1"]},
        "emphasis": {"color": solarized["blue"]},
        "emphasis.strong": {"color": solarized["blue"], "font_weight": 700},
        "enum": {"color": solarized["orange"]},
        "function": {"color": solarized["blue"]},
        "hint": {"color": "#4f8297ff", "font_weight": 700},
        "keyword": {"color": solarized["green"]},
        "label": {"color": solarized["blue"]},
        "link_text": {"color": solarized["blue"], "font_style": "italic"},
        "link_uri": {"color": solarized["violet"]},
        "number": {"color": solarized["magenta"]},
        "operator": {"color": solarized["green"]},
        "predictive": {"color": solarized["fg3"], "font_style": "italic"},
        "preproc": {"color": solarized["orange"]},
        "primary": {"color": solarized["fg1"]},
        "property": {"color": solarized["blue"]},
        "punctuation": {"color": solarized["fg2"]},
        "punctuation.bracket": {"color": solarized["fg2"]},
        "punctuation.delimiter": {"color": solarized["fg2"]},
        "punctuation.list_marker": {"color": solarized["fg2"]},
        "punctuation.special": {"color": solarized["fg2"]},
        "string": {"color": solarized["cyan"]},
        "string.escape": {"color": solarized["fg2"]},
        "string.regex": {"color": solarized["orange"]},
        "string.special": {"color": solarized["orange"]},
        "string.special.symbol": {"color": solarized["orange"]},
        "tag": {"color": solarized["red"]},
        "text.literal": {"color": solarized["cyan"]},
        "title": {"color": solarized["orange"], "font_weight": 700},
        "type": {"color": solarized["yellow"]},
        "variable": {"color": solarized["fg1"]},
        "variant": {"color": solarized["blue"]},
    }
    theme = {
        "background": solarized["bg1"],
        "border": solarized["fg2"],
        "border.disabled": None,
        "border.focused": solarized["fg1"],
        "border.selected": solarized["blue"],
        "border.transparent": None,
        "border.variant": None,
        "conflict": solarized["red"],
        "conflict.background": solarized["bg1"],
        "conflict.border": solarized["red"],
        "created": solarized["green"],
        "created.background": solarized["bg1"],
        "created.border": solarized["green"],
        "deleted": solarized["orange"],
        "deleted.background": solarized["bg1"],
        "deleted.border": solarized["orange"],
        "drop_target.background": solarized["bg2"],
        "editor.active_line.background": solarized["bg2"],
        "editor.active_line_number": solarized["fg1"],
        "editor.active_wrap_guide": solarized["fg2"],
        "editor.background": solarized["bg1"],
        "editor.document_highlight.read_background": solarized["blue"] + "99",
        "editor.document_highlight.write_background": solarized["blue"] + "66",
        "editor.foreground": solarized["fg1"],
        "editor.gutter.background": solarized["bg1"],
        "editor.highlighted_line.background": solarized["bg1"],
        "editor.invisible": solarized["bg2"],
        "editor.line_number": solarized["fg2"],
        "editor.subheader.background": solarized["bg1"],
        "editor.wrap_guide": solarized["bg2"],
        "element.active": solarized["bg2"],
        "element.background": solarized["bg2"],
        "element.disabled": solarized["bg2"],
        "element.hover": solarized["bg2"],
        "element.selected": solarized["blue"] + "66",
        "elevated_surface.background": solarized["bg1"],
        "error": solarized["red"],
        "error.background": solarized["bg1"],
        "error.border": solarized["red"],
        "ghost_element.active": solarized["fg1"],
        "ghost_element.background": solarized["bg1"],
        "ghost_element.disabled": solarized["fg2"],
        "ghost_element.hover": solarized["bg2"],
        "ghost_element.selected": solarized["blue"] + "66",
        "hidden": solarized["fg2"],
        "hidden.background": solarized["bg1"],
        "hidden.border": solarized["bg1"],
        "hint": solarized["fg2"],
        "hint.background": solarized["bg2"],
        "hint.border": solarized["fg2"],
        "icon": solarized["fg1"],
        "icon.accent": solarized["blue"],
        "icon.disabled": solarized["fg2"],
        "icon.muted": solarized["fg2"],
        "icon.placeholder": solarized["fg2"],
        "ignored": solarized["fg2"],
        "ignored.background": solarized["bg1"],
        "ignored.border": solarized["fg2"],
        "info": solarized["blue"],
        "info.background": solarized["bg1"],
        "info.border": solarized["blue"],
        "link_text.hover": solarized["blue"],
        "modified": solarized["yellow"],
        "modified.background": solarized["bg1"],
        "modified.border": solarized["yellow"],
        "pane.focused_border": solarized["fg1"],
        "panel.background": solarized["bg2"],
        "panel.focused_border": solarized["blue"],
        "players": players,
        "predictive": solarized["fg3"],
        "predictive.background": solarized["bg2"],
        "predictive.border": solarized["fg3"],
        "renamed": solarized["magenta"],
        "renamed.background": solarized["bg1"],
        "renamed.border": solarized["magenta"],
        "scrollbar.thumb.border": None,
        "scrollbar.thumb.hover_background": solarized["fg2"],
        "scrollbar.track.background": None,
        "scrollbar.track.border": solarized["bg2"],
        "scrollbar_thumb.background": solarized["bg2"],
        "search.match_background": solarized["yellow"] + "66",
        "status_bar.background": solarized["bg2"],
        "success": solarized["green"],
        "success.background": solarized["bg1"],
        "success.border": solarized["green"],
        "surface.background": solarized["bg1"],
        "syntax": syntax,
        "tab.active_background": solarized["bg1"],
        "tab.inactive_background": solarized["bg2"],
        "tab_bar.background": solarized["bg2"],
        "terminal.ansi.black": solarized["base02"],
        "terminal.ansi.blue": solarized["blue"],
        "terminal.ansi.bright_black": solarized["base03"],
        "terminal.ansi.bright_blue": solarized["base0"],
        "terminal.ansi.bright_cyan": solarized["base1"],
        "terminal.ansi.bright_green": solarized["base01"],
        "terminal.ansi.bright_magenta": solarized["violet"],
        "terminal.ansi.bright_red": solarized["orange"],
        "terminal.ansi.bright_white": solarized["base3"],
        "terminal.ansi.bright_yellow": solarized["base00"],
        "terminal.ansi.cyan": solarized["cyan"],
        "terminal.ansi.dim_black": solarized["base02"],
        "terminal.ansi.dim_blue": solarized["blue"],
        "terminal.ansi.dim_cyan": solarized["cyan"],
        "terminal.ansi.dim_green": solarized["green"],
        "terminal.ansi.dim_magenta": solarized["magenta"],
        "terminal.ansi.dim_red": solarized["red"],
        "terminal.ansi.dim_white": solarized["base2"],
        "terminal.ansi.dim_yellow": solarized["yellow"],
        "terminal.ansi.green": solarized["green"],
        "terminal.ansi.magenta": solarized["magenta"],
        "terminal.ansi.red": solarized["red"],
        "terminal.ansi.white": solarized["base2"],
        "terminal.ansi.yellow": solarized["yellow"],
        "terminal.background": solarized["bg1"],
        "terminal.bright_foreground": solarized["fg3"],
        "terminal.dim_foreground": solarized["fg2"],
        "terminal.foreground": solarized["fg1"],
        "text": solarized["fg1"],
        "text.accent": solarized["fg3"],
        "text.disabled": solarized["fg2"],
        "text.muted": solarized["fg2"],
        "text.placeholder": solarized["fg2"],
        "title_bar.background": solarized["bg2"],
        "toolbar.background": solarized["bg1"],
        "unreachable": solarized["violet"],
        "unreachable.background": solarized["bg1"],
        "unreachable.border": solarized["violet"],
        "warning": solarized["orange"],
        "warning.background": solarized["bg1"],
        "warning.border": solarized["orange"],
    }
    return theme


# Dark

solarized.update(
    {
        "bg1": solarized["base03"],
        "bg2": solarized["base02"],
        "fg1": solarized["base0"],
        "fg2": solarized["base01"],
        "fg3": solarized["base1"],
    }
)

solarized_dark = {
    "appearance": "dark",
    "name": "Solarized Dark",
    "style": solarized_theme(solarized),
}

# Light

solarized.update(
    {
        "bg1": solarized["base3"],
        "bg2": solarized["base2"],
        "fg1": solarized["base00"],
        "fg2": solarized["base1"],
        "fg3": solarized["base01"],
    }
)
solarized_light = {
    "appearance": "light",
    "name": "Solarized Light",
    "style": solarized_theme(solarized),
}

solarized_dict = {
    "$schema": "https://zed.dev/schema/themes/v0.1.0.json",
    "author": "harmtemolder",
    "name": "Solarized",
    "themes": [solarized_dark, solarized_light],
}

with open("themes/solarized.json", "w") as solarized_json:
    json.dump(solarized_dict, solarized_json, indent=2)
