from datetime import datetime
from dooit.ui.api import DooitAPI, timer
from ._base import BarUtilWidgetBase


def get_clock_wrapper(format: str):
    @timer(1)
    def get_clock(*_) -> str:
        return datetime.now().strftime(format)

    return get_clock


class Clock(BarUtilWidgetBase):
    def __init__(
        self,
        api: DooitAPI,
        fmt: str = " {} ",
        format: str = "%H:%M:%S",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(
            func=get_clock_wrapper(format), width=None, api=api, fmt=fmt, fg=fg, bg=bg
        )
