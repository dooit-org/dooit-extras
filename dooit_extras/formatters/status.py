from typing import Callable
from rich.text import Text
from dooit.api import Todo
from dooit.ui.api import DooitAPI


def status_icons(completed="x", pending="o", overdue="!", fmt="{}") -> Callable:
    """
    Shows status icons for todos
    """

    def wrapper(status: str, _: Todo, api: DooitAPI) -> Text:
        """
        Shows icon for various statuses
        """

        theme = api.vars.theme
        if status == "completed":
            icon = completed
            style = theme.green
        elif status == "pending":
            icon = pending
            style = theme.yellow
        else:
            icon = overdue
            style = theme.red

        return Text.from_markup(fmt.format(icon), style=style)

    return wrapper
