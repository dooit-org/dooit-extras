from typing import Callable, Optional
from dooit.ui.api import DooitAPI
from rich.style import Style
from rich.text import Text, TextType
from dooit.ui.widgets.bars import StatusBarWidget


class BarUtilWidgetBase(StatusBarWidget):
    """
    Base Widget for all Bar Utils Widgets
    """

    def __init__(
        self,
        func: Callable,
        width: Optional[int],
        api: DooitAPI,
        text_left: str = "",
        text_right: str = "",
        reverse_pads: bool = True,
    ):
        super().__init__(func, width)
        self.api = api
        self.text_left = text_left
        self.text_right = text_right
        self.reverse_pads = reverse_pads

    def reversed_style(self, style: Style) -> Style:
        return Style(color=style.bgcolor, bgcolor=style.color)

    @property
    def raw_text(self) -> str:
        value = self.value

        if isinstance(value, Text):
            return value.markup

        return value

    def get_main_text(self) -> Text:
        return Text(self.raw_text)

    def render_text(
        self,
        text: str,
        style: Style,
    ) -> Text:
        # Revert colors for decorations
        pad_style = self.reversed_style(style) if self.reverse_pads else style

        text_left = Text(
            self.text_left,
            style=pad_style,
        )
        text_right = Text(
            self.text_right,
            style=pad_style,
        )
        main_text = Text(text, style=style)

        return Text.assemble(text_left, main_text, text_right)

    def render(self) -> TextType:
        return self.value
