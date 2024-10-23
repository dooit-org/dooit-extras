from dooit.ui.api import DooitAPI
from dooit.ui.api.events import subscribe
from dooit.ui.api.plug import Startup
from rich.text import Text
from rich.style import Style

from ._base import BarUtilWidgetBase


def text_wrapper(text: str):

    @subscribe(Startup)
    def wrapper(*_):
        return text

    return wrapper


class TextBox(BarUtilWidgetBase):
    def __init__(
        self,
        api: DooitAPI,
        text: str,
        fmt: str = " {} ",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(func=text_wrapper(text), width=None, api=api, fmt=fmt)

        self.fg = fg
        self.bg = bg

    def render(self) -> Text:
        fg = self.fg or self.api.app.current_theme.background_1
        bg = self.bg or self.api.app.current_theme.primary
        style = Style(color=fg, bgcolor=bg)

        return self.render_text(style=style)
