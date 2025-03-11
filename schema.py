#!/usr/bin/env

import json

with open("schema.json") as schema_json:
    schema = json.load(schema_json)

prefix = '        "'
suffix = '": solarized[""] + "ff",'

print(
    prefix
    + f"{suffix}\n{prefix}".join(
        list(schema["definitions"]["ThemeStyleContent"]["properties"].keys())
    )
    + suffix
)
