from typing import Union, Optional
from dooit.api import Todo, Workspace
from rich.style import Style
from dooit.ui.api import DooitAPI
from rich.style import Style
from rich.text import Text
from dooit.ui.api import DooitAPI, extra_formatter
import re

ModelType = Union[Todo, Workspace]


def description_highlight_link(color: Optional[str] = None):
    @extra_formatter
    def wrapper(value: str, _, api: DooitAPI):
        """
        Highlight URLs in the description.
        """

        url_pattern = re.compile(
            r"http[s]?://"
            r"(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|"
            r"(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            re.IGNORECASE,
        )

        text = Text.from_markup(value)
        text.highlight_regex(
            url_pattern,
            style=Style(
                color=color or api.vars.theme.primary,
                underline=True,
                italic=True,
            ),
        )

        return text.markup

    return wrapper


def description_children_count(format: str = " ({}) "):
    @extra_formatter
    def wrapper(value: str, model: ModelType):
        """
        Highlight the number of children in the description.
        """

        if isinstance(model, Todo):
            children_count = len(model.todos)
        else:
            children_count = len(model.workspaces)

        if not children_count:
            return

        return value + format.format(children_count)

    return wrapper


def description_strike_completed(dim: bool = True):
    @extra_formatter
    def wrapper(value: str, todo: Todo):
        if todo.is_completed:
            return Text(value, style=Style(strike=True, dim=dim)).markup

    return wrapper


def todo_description_progress(fmt=" ({completed_percent}%)"):
    @extra_formatter
    def wrapper(value: str, todo: Todo):
        if not todo.todos:
            return

        total_count = len(todo.todos)

        completed_count = len([t for t in todo.todos if t.is_completed])
        remaining_count = total_count - completed_count

        completed_percent = int(round((completed_count / total_count) * 100))
        remaining_percent = 100 - completed_percent

        data = dict(
            total_count=total_count,
            completed_count=completed_count,
            remaining_count=remaining_count,
            completed_percent=completed_percent,
            remaining_percent=remaining_percent,
        )

        return value + fmt.format(**data)

    return wrapper
