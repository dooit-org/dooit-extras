from typing import Callable, Optional
from dooit.ui.api import DooitAPI
from dooit.api.theme import DooitThemeBase
from rich.style import Style, StyleType
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
        fmt: TextType = "{}",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(func, width)
        self.api = api
        self.fmt = fmt
        self.fg = fg
        self.bg = bg

    @property
    def theme(self) -> DooitThemeBase:
        return self.api.vars.theme

    def rich_value(self) -> Text:
        return Text.from_markup(self.value)

    @property
    def value(self) -> str:
        if isinstance(self.fmt, Text):
            self.fmt = self.fmt.markup

        return self.fmt.format(super().value)

    def render_text(
        self, value: Optional[TextType] = None, style: StyleType = ""
    ) -> Text:
        if not value:
            value = self.rich_value()

        if isinstance(value, str):
            value = Text.from_markup(value)

        value.stylize(style)

        # Because the stylize method above will ignore other embedded styles
        return Text.from_markup(value.markup)

    def render(self) -> Text:
        fg = self.fg or self.api.vars.theme.background1
        bg = self.bg or self.api.vars.theme.primary
        style = Style(color=fg, bgcolor=bg)

        return self.render_text(style=style)
