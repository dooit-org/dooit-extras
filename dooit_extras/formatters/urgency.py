from typing import Callable, Dict
from rich.style import StyleType, Style
from rich.text import Text
from dooit.api import Todo
from dooit.ui.api import DooitAPI


def urgency_icons(
    icons: Dict[int, str] = {}, colors: Dict[int, StyleType] = {}, fmt="{}"
) -> Callable:
    """
    Shows urgency icons for todos
    """

    def wrapper(urgency: int, todo: Todo, api: DooitAPI) -> Text:
        """
        Shows icon for various urgency levels (1-4)
        """

        theme = api.vars.theme
        default_styles = {
            1: Style(color=theme.green, bold=True),
            2: Style(color=theme.yellow, bold=True),
            3: Style(color=theme.orange, bold=True),
            4: Style(color=theme.red, bold=True),
        }

        default_icons = {
            1: "󰲠",  # Low urgency
            2: "󰲢",  # Medium urgency
            3: "󰲤",  # High urgency
            4: "󰲦",  # Critical urgency
        }

        default_styles.update(colors)
        default_icons.update(icons)

        icon = default_icons[urgency]
        style = default_styles[urgency]

        return Text.from_markup(fmt.format(icon), style=style)

    return wrapper
