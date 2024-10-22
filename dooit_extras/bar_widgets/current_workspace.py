from typing import Union
from dooit.ui.api import DooitAPI
from dooit.ui.api.events import subscribe
from dooit.ui.events.events import Startup, WorkspaceSelected
from rich.text import Text
from rich.style import Style

from ._base import BarUtilWidgetBase


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


class CurrentWorkspace(BarUtilWidgetBase):
    def __init__(
        self,
        api: DooitAPI,
        no_workspace_text="No Workspace Selected",
        fmt=" {} ",
        fg: str = "",
        bg: str = "",
    ) -> None:
        super().__init__(
            func=get_workspace_name_wrapper(no_workspace_text),
            api=api,
            width=None,
            fmt=fmt,
        )

        self.fg = fg
        self.bg = bg

    def render(self) -> Text:
        fg = self.fg or self.api.app.current_theme.background_1
        bg = self.bg or self.api.app.current_theme.primary
        style = Style(color=fg, bgcolor=bg)

        return self.render_text(style=style)
