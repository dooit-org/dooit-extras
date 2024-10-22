from datetime import datetime
from dooit.ui.api import DooitAPI
from dooit.ui.api.events import timer
from rich.text import Text
from rich.style import Style

from ._base import BarUtilWidgetBase


@timer(1)
def get_clock(api: DooitAPI, *_) -> str:
    return ""


class Clock(BarUtilWidgetBase):
    def __init__(
        self,
        api: DooitAPI,
        fmt: str = " {} ",
        format: str = "%H:%M:%S",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(func=lambda: None, width=None, api=api, fmt=fmt)

        self.format = format
        self.fg = fg
        self.bg = bg

    @property
    def value(self) -> str:
        return self.fmt.format(datetime.now().strftime(self.format))

    def render(self) -> Text:
        fg = self.fg or self.api.app.current_theme.background_1
        bg = self.bg or self.api.app.current_theme.primary
        style = Style(color=fg, bgcolor=bg)

        return self.render_text(style=style)
