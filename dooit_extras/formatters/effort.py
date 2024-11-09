from typing import Optional
from rich.style import Style
from rich.text import Text
from dooit.api import Todo
from dooit.ui.api import DooitAPI, extra_formatter


def effort_icon(
    icon: str = "󰈸 ",
    color: Optional[str] = None,
    show_on_zero: bool = True,
):
    @extra_formatter
    def wrapper(value: str, model: Todo, api: DooitAPI):
        theme = api.vars.theme

        if not show_on_zero and model.effort == 0:
            return ""

        return (
            Text()
            + Text.from_markup(icon, style=Style(color=color or theme.orange))
            + value
        )

    return wrapper
