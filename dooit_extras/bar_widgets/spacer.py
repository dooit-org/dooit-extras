from dooit.ui.api import DooitAPI
from ._base import BarUtilWidgetBase


class Spacer(BarUtilWidgetBase):
    def __init__(self, api: DooitAPI, width: int, fg: str = "", bg: str = "") -> None:
        super().__init__(func=lambda *_: "", width=width, api=api, fg=fg, bg=bg)
