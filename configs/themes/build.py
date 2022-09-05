#!/usr/bin/env python3
import os
import pathlib
import sys


def make_css_format(colors: dict) -> list:
    res = []
    for n, v in colors.items():
        res.append("@define-color {} {};\n".format(n, v))
    return res


def make_sway_format(colors: dict) -> list:
    res = []
    for n, v in colors.items():
        res.append("set ${} {}\n".format(n, v))
    return res


def make_rofi_format(colors: dict) -> list:
    res = ["* {\n"]
    for n, v in colors.items():
        res.append("\t{}: {};\n".format(n, v))
    res.append("}")
    return res


def make_mako_format(colors: dict) -> list:
    res = [
        "sort=-time\n",
        "layer=overlay\n",
        "background-color={}\n".format(colors[COLOR_SURFACE]),

        "width=400\n",
        "height=600\n",

        "border-size=2\n",
        "border-color={}\n".format(colors[COLOR_PRIMARY]),

        "icons=0\n",
        "max-icon-size=64\n",
        "default-timeout=5000\n",
        "ignore-timeout=1\n",
        "font=monospace 14\n",
        "\n[urgency=low]\n",
        "border-color={}\n".format(colors[COLOR_PRIMARY]),
        "\n[urgency=normal]\n",
        "border-color={}\n".format(colors[COLOR_SECONDARY]),
        "\n[urgency=high]\n",
        "border-color={}\n".format(colors[COLOR_ERROR]),
        "default-timeout=0\n",
    ]
    return res


COLOR_PRIMARY = "colorPrimary"
COLOR_ON_PRIMARY = "colorOnPrimary"

COLOR_SECONDARY = "colorSecondary"

COLOR_ERROR = "colorError"

COLOR_BACKGROUND = "colorBackground"
COLOR_ON_BACKGROUND = "colorOnBackground"

COLOR_SURFACE = "colorSurface"

REQUIRED_COLORS = [
    COLOR_PRIMARY,
    COLOR_ON_PRIMARY,
    'colorPrimaryContainer',
    'colorOnPrimaryContainer',

    COLOR_SECONDARY,
    'colorOnSecondary',
    'colorSecondaryContainer',
    'colorOnSecondaryContainer',

    COLOR_ERROR,
    'colorOnError',
    'colorErrorContainer',
    'colorOnErrorContainer',

    COLOR_BACKGROUND,
    COLOR_ON_BACKGROUND,
    'colorOutline',

    COLOR_SURFACE,
    'colorOnSurface',
    'colorSurfaceVariant',
    'colorOnSurfaceVariant',
]


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("error: not colors file specified")
        exit(1)

    fileName = sys.argv[1]
    print("info: got file with name '{}'".format(fileName))
    if ".colors" not in fileName:
        print("error: colors file must contains '.color' postfix in the file name")
        exit(1)

    with open(pathlib.PurePath(sys.argv[1])) as color_file:
        lines = {}

        rawLines = color_file.readlines()
        for rawLine in rawLines:
            rawLine = rawLine[:-1]
            if rawLine == "":
                continue
            name, color = rawLine.split(":")
            lines[name] = color

        for required in REQUIRED_COLORS:
            if required not in lines:
                print("error: required color '{}'".format(required))
                exit(1)

    build_dir = os.getenv("BUILD_DIR")
    if not build_dir:
        build_dir = "build"

    # SWAY
    with open(pathlib.Path(build_dir).joinpath("02-colors.conf"), "w") as sway_file:
        sway_file.writelines(make_sway_format(lines))

    # CSS
    with open(pathlib.Path(build_dir).joinpath("colors.css"), "w") as css_file:
        css_file.writelines(make_css_format(lines))

    # Rofi
    with open(pathlib.Path(build_dir).joinpath("colors.rasi"), "w") as rofi_file:
        rofi_file.writelines(make_rofi_format(lines))

    # Mako
    with open(pathlib.Path(build_dir).joinpath("mako"), "w") as mako_file:
        mako_file.writelines(make_mako_format(lines))
