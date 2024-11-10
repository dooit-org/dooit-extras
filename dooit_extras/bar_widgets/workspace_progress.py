from typing import Union
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import WorkspaceSelected, TodoEvent
from dooit.api import Workspace
from .text_poller import Custom


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


class WorkspaceProgress(Custom):
    def __init__(self, api: DooitAPI, fmt="{}", fg: str = "", bg: str = "") -> None:
        super().__init__(
            api=api,
            function=get_workspace_completion,
            width=None,
            fmt=fmt,
            fg=fg,
            bg=bg,
        )
