from dooit.ui.api import DooitAPI
from dooit.ui.api.events import subscribe
from dooit.ui.api.plug import Startup
from rich.text import TextType
from ._base import BarUtilWidgetBase


def text_wrapper(text: TextType):
    @subscribe(Startup)
    def wrapper(*_):
        return text

    return wrapper


class TextBox(BarUtilWidgetBase):
    def __init__(
        self,
        api: DooitAPI,
        text: TextType,
        fmt: str = "{}",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(
            func=text_wrapper(text), width=None, api=api, fmt=fmt, fg=fg, bg=bg
        )
