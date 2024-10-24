from collections import defaultdict
from typing import Dict
from dooit.ui.tui import DooitThemeBase
from rich.style import Style
from rich.text import Text
from ._base import BarUtilWidgetBase
from dooit.ui.api import DooitAPI
from dooit.ui.api.events import subscribe
from dooit.ui.events import ModeChanged


def get_mode_wrapper(mode_styles: Dict[str, Style], fmt: str):
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

    @subscribe(ModeChanged)
    def get_mode(api: DooitAPI, _: ModeChanged):
        mode = api.app._mode
        styles_dict = get_default_mode_styles(api.vars.theme) | mode_styles

        return Text(fmt.format(mode), style=styles_dict[mode])

    return get_mode


class Mode(BarUtilWidgetBase):
    """
    Mode Bar Widget to show mode
    """

    def __init__(
        self,
        api: DooitAPI,
        fmt=" {} ",
        mode_styles: Dict[str, Style] = {},
    ) -> None:
        super().__init__(
            func=get_mode_wrapper(mode_styles, fmt),
            width=None,
            api=api,
        )

    def render(self) -> Text:
        return self.rich_value()
