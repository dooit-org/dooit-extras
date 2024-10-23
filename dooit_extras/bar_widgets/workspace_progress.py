from typing import Union
from dooit.ui.api.events import subscribe
from dooit.ui.api import DooitAPI
from dooit.ui.events import WorkspaceSelected, TodoEvent
from dooit.api import Workspace
from ._base import BarUtilWidgetBase


def get_completed(workspace: Workspace):
    """
    Get the percentage of completed todos in the workspace
    """

    todos = workspace.todos

    if not todos:
        return 0

    complete_count = sum(t.is_completed for t in todos)
    total_count = len(todos)

    return int(100 * complete_count / total_count)


@subscribe(WorkspaceSelected, TodoEvent)
def get_workspace_completion(
    api: DooitAPI,
    event: Union[WorkspaceSelected, TodoEvent],
) -> str:
    if isinstance(event, WorkspaceSelected):
        workspace = event.workspace
    elif isinstance(event, TodoEvent):
        workspace = api.app.workspace_tree.current_model

    return str(get_completed(workspace))


class WorkspaceProgress(BarUtilWidgetBase):
    def __init__(self, api: DooitAPI, fmt="{}", fg: str = "", bg: str = "") -> None:
        super().__init__(
            func=get_workspace_completion, width=None, api=api, fmt=fmt, fg=fg, bg=bg
        )
