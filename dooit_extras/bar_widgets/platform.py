from collections import defaultdict
from dooit.ui.api import DooitAPI
from dooit.api.theme import DooitThemeBase
from rich.text import Text, TextType
from rich.style import Style
from .text_box import TextBox

import platform
import os


class PlatformInfo:
    def __init__(self, icon: str, color: str) -> None:
        self.icon = icon
        self.color = color

    @classmethod
    def default(cls) -> "PlatformInfo":
        return cls("", "red")


ICONS: defaultdict[str, PlatformInfo] = defaultdict(PlatformInfo.default)


def get_user_platform(theme: DooitThemeBase, icon: bool) -> TextType:
    default_icons = {
        "Windows": PlatformInfo("", theme.blue),
        "macOS": PlatformInfo("", theme.foreground3),
        "Linux": PlatformInfo("", theme.yellow),
        "NixOS": PlatformInfo("", theme.cyan),
        "Arch Linux": PlatformInfo("", theme.blue),
        "Ubuntu": PlatformInfo("", theme.orange),
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
        icon_info = ICONS[system]
        text += Text(
            icon_info.icon,
            style=Style(color=icon_info.color),
        )

    text.append(" " + system)
    return text


class Platform(TextBox):
    def __init__(
        self,
        api: DooitAPI,
        icon: bool = True,
        fmt: str = " {} ",
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
