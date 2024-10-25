from typing import Callable, Dict
from rich.style import Style
from rich.text import Text
from dooit.api import Todo
from dooit.ui.api import DooitAPI


def status_icons(
    icons: Dict[str, str] = {}, colors: Dict[str, Style] = {}, fmt="{}"
) -> Callable:
    """
    Shows status icons for todos
    """

    def wrapper(status: str, _: Todo, api: DooitAPI) -> Text:
        """
        Shows icon for various statuses
        """

        theme = api.vars.theme
        default_styles = {
            "completed": Style(color=theme.green, bold=True),
            "pending": Style(color=theme.yellow, bold=True),
            "overdue": Style(color=theme.red, bold=True),
        }

        default_icons = {
            "completed": "x",
            "pending": "o",
            "overdue": "!",
        }

        default_styles.update(colors)
        default_icons.update(icons)

        icon = default_icons[status]
        style = default_styles[status]

        return Text(fmt.format(icon), style=style)

    return wrapper
