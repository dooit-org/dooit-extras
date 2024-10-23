from dooit.ui.api import DooitAPI
from .clock import Clock


class Date(Clock):
    def __init__(
        self,
        api: DooitAPI,
        fmt: str = " {} ",
        format: str = "%b %d",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(api=api, format=format, fmt=fmt, fg=fg, bg=bg)
