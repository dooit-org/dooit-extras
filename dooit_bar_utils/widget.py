from typing import Callable, Optional
from rich.style import Style
from rich.text import Text
from dooit.ui.widgets.bars import StatusBarWidget


class BarUtilWidgetBase(StatusBarWidget):
    """
    Base Widget for all Bar Utils Widgets
    """

    def __init__(
        self,
        func: Callable,
        width: Optional[int],
        text_left: str = "",
        text_right: str = "",
        fg: str = "black",
        bg: str = "white",
        reverse_pads: bool = True,
    ):
        super().__init__(func, width)
        self.text_left = text_left
        self.text_right = text_right
        self.color_fg = fg
        self.color_bg = bg
        self.reverse_pads = reverse_pads

    def get_style(self, reversed: bool = False) -> Style:
        return (
            Style(color=self.color_fg, bgcolor=self.color_bg)
            if not reversed
            else Style(color=self.color_bg, bgcolor=self.color_fg)
        )

    def _get_raw_main_text(self) -> str:
        value = self.value

        if isinstance(value, Text):
            return value.markup

        return value

    def get_main_text(self) -> Text:
        return Text(self._get_raw_main_text(), style=self.get_style())

    def render(self) -> Text:
        # Revert colors for decorations
        text_left = Text(
            self.text_left,
            style=self.get_style(reversed=self.reverse_pads),
        )
        text_right = Text(
            self.text_right,
            style=self.get_style(reversed=not self.reverse_pads),
        )

        main_text = self.get_main_text()

        return Text.assemble(text_left, main_text, text_right)
