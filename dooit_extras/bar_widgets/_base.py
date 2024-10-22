from typing import Callable, Optional
from dooit.ui.api import DooitAPI
from dooit.ui.tui import DooitThemeBase
from rich.style import StyleType
from rich.text import Text, TextType
from dooit.ui.widgets.bars import StatusBarWidget


class BarUtilWidgetBase(StatusBarWidget):
    """
    Base Widget for all Bar Utils Widgets
    """

    def __init__(self, func: Callable, width: Optional[int], api: DooitAPI, fmt="{}"):
        super().__init__(func, width)
        self.api = api
        self.fmt = fmt

    @property
    def theme(self) -> DooitThemeBase:
        return self.api.vars.theme

    def rich_value(self) -> Text:
        return Text.from_markup(self.value)

    @property
    def value(self) -> str:
        return self.fmt.format(super().value)

    def render_text(
        self, value: Optional[TextType] = None, style: StyleType = ""
    ) -> Text:
        if not value:
            value = self.rich_value()

        if isinstance(value, str):
            value = Text.from_markup(value)

        value.stylize(style)
        return value

    def render(self) -> Text:
        return self.rich_value()
