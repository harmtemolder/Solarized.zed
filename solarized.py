#!/usr/bin/env python

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

solarized.update(
    {
        "accent": solarized["blue"],
    }
)


def solarized_theme(solarized):
    theme = {}
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
    "$schema": "https: #zed.dev/schema/themes/v0.1.0.json",
    "author": "harmtemolder",
    "name": "Solarized",
    "themes": [solarized_dark, solarized_light],
}

with open("themes/solarized.json", "w") as solarized_json:
    json.dump(solarized_dict, solarized_json, indent=2)
