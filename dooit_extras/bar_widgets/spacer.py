from dooit.ui.api import DooitAPI
from rich.text import Text
from rich.style import Style

from ._base import BarUtilWidgetBase


class Spacer(BarUtilWidgetBase):
    def __init__(self, api: DooitAPI, width: int, fg: str = "", bg: str = "") -> None:
        super().__init__(func=lambda: " ", width=width, api=api)

        self.fg = fg
        self.bg = bg

    def render(self) -> Text:
        fg = self.fg or self.api.app.current_theme.background_1
        bg = self.bg or self.api.app.current_theme.primary
        style = Style(color=fg, bgcolor=bg)

        return self.render_text(style=style)
