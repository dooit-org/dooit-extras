from collections import defaultdict
from typing import Dict
from dooit.ui.tui import DooitThemeBase
from rich.style import Style
from rich.text import Text
from ._base import BarUtilWidgetBase
from dooit.ui.api import DooitAPI
from dooit.ui.api.events import subscribe
from dooit.ui.events import ModeChanged


@subscribe(ModeChanged)
def get_mode(api: DooitAPI, _: ModeChanged):
    return api.app._mode


def get_default_mode_styles(theme: DooitThemeBase) -> Dict[str, Style]:
    fg = theme.background_1
    modes = defaultdict(lambda: Style(color=fg, bgcolor=theme.primary))

    extra_styles = dict(
        NORMAL=Style(color=fg, bgcolor=theme.primary),
        INSERT=Style(color=fg, bgcolor=theme.secondary),
    )

    for mode, style in extra_styles.items():
        modes[mode] = style

    return modes


class Mode(BarUtilWidgetBase):
    """
    Mode Bar Widget to show mode
    """

    def __init__(self, api: DooitAPI, mode_styles: Dict[str, Style] = {}) -> None:
        super().__init__(func=get_mode, width=None, api=api)

        self.mode_styles = get_default_mode_styles(api.app.current_theme) | mode_styles

    def render(self) -> Text:
        style = self.mode_styles[self.value]
        return self.render_text(style=style)
