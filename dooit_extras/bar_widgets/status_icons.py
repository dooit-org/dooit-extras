from rich.text import Text
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import TodoEvent, WorkspaceSelected
from .text_poller import Custom


def get_status_icons(completed_icon, pending_icon, overdue_icon):
    @subscribe(TodoEvent, WorkspaceSelected)
    def wrapper(api: DooitAPI, _):
        workspace = api.vars.current_workspace
        if not workspace:
            return ""

        theme = api.vars.theme

        completed = sum([i.is_completed for i in workspace.todos])
        pending = sum([i.is_pending for i in workspace.todos])
        overdue = sum([i.is_overdue for i in workspace.todos])

        return (
            Text()
            + Text.from_markup(completed_icon + str(completed), style=theme.green)
            + Text(" ")
            + Text.from_markup(pending_icon + str(pending), style=theme.yellow)
            + Text(" ")
            + Text.from_markup(overdue_icon + str(overdue), style=theme.red)
        )

    return wrapper


class StatusIcons(Custom):
    def __init__(
        self,
        api: DooitAPI,
        completed_icon=" ",
        pending_icon=" ",
        overdue_icon=" ",
        fmt: str = " {} ",
        bg: str = "",
    ) -> None:
        super().__init__(
            api,
            get_status_icons(completed_icon, pending_icon, overdue_icon),
            None,
            fmt,
            "",
            bg or api.vars.theme.background3,
        )
