from typing import Union
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup, WorkspaceSelected
from .text_poller import Custom


def get_workspace_name_wrapper(no_workspace_text: str):
    @subscribe(WorkspaceSelected, Startup)
    def get_workspace_name(
        _: DooitAPI, event: Union[WorkspaceSelected, Startup]
    ) -> str:
        if isinstance(event, Startup):
            return no_workspace_text

        text = event.workspace.description
        parent = event.workspace.parent_workspace

        if parent and not parent.is_root:
            text = f"{parent.description}/{text}"

        return text

    return get_workspace_name


class CurrentWorkspace(Custom):
    def __init__(
        self,
        api: DooitAPI,
        no_workspace_text="No Workspace Selected",
        fmt=" {} ",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(
            api=api,
            function=get_workspace_name_wrapper(no_workspace_text),
            width=None,
            fmt=fmt,
        )

        self.fg = fg
        self.bg = bg
