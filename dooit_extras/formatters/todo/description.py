from rich.style import Style
from rich.text import Text
from dooit.api import Todo
from dooit.ui.api import DooitAPI, allow_multiple_formatting
import re

url_pattern = re.compile(
    r"http[s]?://"
    r"(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|"
    r"(?:%[0-9a-fA-F][0-9a-fA-F]))+",
    re.IGNORECASE,
)


@allow_multiple_formatting
def highlight_link(value: str, todo: Todo, api: DooitAPI):
    text = Text.from_markup(value)
    text.highlight_regex(
        url_pattern,
        style=Style(
            color=api.vars.theme.primary,
            underline=True,
            italic=True,
        ),
    )

    return text.markup
