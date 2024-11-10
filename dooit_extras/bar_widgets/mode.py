from rich.text import Text, TextType
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import ModeChanged
from .text_poller import Custom


def get_mode_wrapper(
    format_normal: TextType,
    format_insert: TextType,
):
    @subscribe(ModeChanged)
    def wrapper(_: DooitAPI, event: ModeChanged):
        mode = event.mode

        if mode == "NORMAL":
            text = format_normal
        elif mode == "INSERT":
            text = format_insert
        else:
            text = mode

        if isinstance(text, Text):
            text = text.markup

        return text

    return wrapper


class Mode(Custom):
    """
    Mode Bar Widget to show mode
    """

    def __init__(
        self,
        api: DooitAPI,
        format_normal: TextType = " NORMAL ",
        format_insert: TextType = " INSERT ",
        fmt="{}",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(
            api=api,
            function=get_mode_wrapper(format_normal, format_insert),
            width=None,
            fmt=fmt,
            fg=fg,
            bg=bg,
        )
