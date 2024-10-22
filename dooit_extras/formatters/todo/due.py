from typing import Optional
from dooit.api.todo import datetime, Todo


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
