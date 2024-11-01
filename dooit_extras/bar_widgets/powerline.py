from dooit.ui.api import DooitAPI
from dooit.ui.tui import Dooit
from .text_box import TextBox
from typing_extensions import Self


class Powerline(TextBox):
    def __init__(
        self,
        api: DooitAPI = DooitAPI(Dooit()),
        text: str = "",
        fmt: str = "{}",
        fg: str = "",
        bg: str = "",
    ) -> None:
        bg = bg or api.vars.theme.background2
        super().__init__(api, text, fmt, fg, bg)

    # Lower Triangles
    @classmethod
    def lower_left_triangle(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    @classmethod
    def lower_right_triangle(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    # Upper Triangles
    @classmethod
    def upper_left_triangle(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    @classmethod
    def upper_right_triangle(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    # Arrows
    @classmethod
    def right_arrow(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    @classmethod
    def left_arrow(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    # Rounded
    @classmethod
    def right_rounded(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    @classmethod
    def left_rounded(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    # Ice
    @classmethod
    def left_ice(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, " ", fg=fg, bg=bg)

    @classmethod
    def right_ice(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, "", fg=fg, bg=bg)

    # Fire
    @classmethod
    def left_flame(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, " ", fg=fg, bg=bg)

    @classmethod
    def right_flame(cls, api: DooitAPI, fg: str = "", bg: str = "") -> Self:
        return cls(api, " ", fg=fg, bg=bg)
