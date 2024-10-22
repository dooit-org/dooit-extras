from typing import Optional
from rich.style import Style
from rich.text import Text
from dooit.api.todo import datetime, Todo
from dooit.ui.api import DooitAPI


def causal_date_format(due: Optional[datetime], _: Todo) -> str:
    if not due:
        return ""

    current_year = datetime.now().year
    dt_format = "%b %d"

    if due.year != current_year:
        dt_format += " '%y"

    if due.hour != 0 or due.minute != 0:
        dt_format += " (%-I:%M)"

    return due.strftime(dt_format)


def danger_today(due: Optional[datetime], _: Todo, api: DooitAPI) -> Optional[str]:
    if not due:
        return ""

    if due.date() == datetime.today().date():
        return Text(
            "Today",
            style=Style(
                color=api.vars.theme.red,
                bold=True,
            ),
        ).markup
