from typing import Callable, Optional
from rich.style import Style
from dooit.api.todo import datetime, Todo
from dooit.ui.api import DooitAPI, extra_formatter
from rich.text import Text


def due_casual_format(fmt="{}") -> Callable:
    def wrapper(due: Optional[datetime], _: Todo) -> str:
        """
        Shows the date in a more simple format:
        Example: `23 Oct` instead of `23-10-2024`
        """

        if not due:
            return ""

        current_year = datetime.now().year
        dt_format = "%b %d"

        if due.year != current_year:
            dt_format += " '%y"

        if due.hour != 0 or due.minute != 0:
            dt_format += " (%H:%M)"

        return fmt.format(due.strftime(dt_format))

    return wrapper


def due_danger_today(fmt: str = "{}") -> Callable:
    def wrapper(due: Optional[datetime], _: Todo, api: DooitAPI) -> Optional[str]:
        """
        If the due date is today, show a bold red "Today" text.
        """

        if not due:
            return ""

        if due.date() == datetime.today().date():
            return Text(
                fmt.format("Today"),
                style=Style(
                    color=api.vars.theme.red,
                    bold=True,
                ),
            ).markup

    return wrapper


def due_icon(completed: str = "󰃯 ", pending: str = "󰃰 ", overdue: str = " "):
    @extra_formatter
    def wrapper(due: str, model: Todo, api: DooitAPI):
        theme = api.vars.theme
        if not model.due:
            return due

        if model.is_completed:
            icon = completed
            color = theme.green

        elif model.is_overdue:
            icon = overdue
            color = theme.red
        else:
            icon = pending
            color = theme.yellow

        return Text() + Text.from_markup(icon, style=Style(color=color)) + due

    return wrapper
