from typing import Optional
from rich.style import Style
from rich.text import Text
from dooit.api import Todo
from dooit.ui.api import DooitAPI, extra_formatter


def recurrence_icon(icon: str = "󰑖 ", color: Optional[str] = None):
    @extra_formatter
    def wrapper(value: str, model: Todo, api: DooitAPI):
        theme = api.vars.theme

        if not model.recurrence:
            return value

        return (
            Text()
            + Text.from_markup(icon, style=Style(color=color or theme.primary))
            + value
        )

    return wrapper
