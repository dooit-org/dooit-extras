from collections import defaultdict
from dooit.ui.api import DooitAPI
from dooit.ui.tui import DooitThemeBase
from rich.text import Text, TextType
from rich.style import Style
from .text_box import TextBox

import platform
import os

ICONS = defaultdict(lambda: ("", "red"))


def get_user_platform(theme: DooitThemeBase, icon: bool) -> TextType:
    default_icons = {
        "Windows": ("", theme.blue),
        "macOS": ("", theme.foreground_3),
        "Linux": ("", theme.yellow),
        "NixOS": ("", theme.cyan),
        "Arch Linux": ("", theme.blue),
        "Ubuntu": ("", theme.orange),
    }

    ICONS.update(default_icons)

    system = platform.system()
    if system == "Linux":
        try:
            os_release = platform.freedesktop_os_release()
            system = os_release.get("NAME", "Linux")
        except AttributeError:
            if os.path.isfile("/etc/os-release"):
                with open("/etc/os-release") as f:
                    for line in f:
                        if line.startswith("NAME="):
                            system = line.strip().split("=")[1].strip('"')
            system = "Linux"
    else:
        system = "Unknown"

    text = Text()
    if icon:
        text.append(Text(ICONS[system][0], style=Style(color=ICONS[system][1])))

    text.append(" " + system)
    return text


class Platform(TextBox):
    def __init__(
        self,
        api: DooitAPI,
        icon: bool = True,
        fmt: str = "{}",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(
            api,
            get_user_platform(api.vars.theme, icon),
            fmt,
            fg,
            bg,
        )
