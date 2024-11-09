from typing import Callable
from rich.text import Text
from dooit.api import Todo
from dooit.ui.api import DooitAPI


def status_icons(
    completed_icon="x", pending_icon="o", overdue_icon="!", fmt="{}"
) -> Callable:
    """
    Shows status icons for todos
    """

    def wrapper(status: str, _: Todo, api: DooitAPI) -> Text:
        """
        Shows icon for various statuses
        """

        theme = api.vars.theme
        if status == "completed":
            icon = completed_icon
            style = theme.green
        elif status == "pending":
            icon = pending_icon
            style = theme.yellow
        else:
            icon = overdue_icon
            style = theme.red

        return Text.from_markup(fmt.format(icon), style=style)

    return wrapper
