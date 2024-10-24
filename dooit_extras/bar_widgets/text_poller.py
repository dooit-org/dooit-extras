from typing import Callable, Optional
from dooit.ui.api import DooitAPI
from ._base import BarUtilWidgetBase


class Custom(BarUtilWidgetBase):
    def __init__(
        self,
        api: DooitAPI,
        function: Callable,
        width: Optional[int] = None,
        fmt: str = " {} ",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(func=function, width=width, api=api, fmt=fmt, fg=fg, bg=bg)
