from datetime import datetime
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

    @property
    def value(self) -> str:
        return self.fmt.format(datetime.now().strftime(self.format))
