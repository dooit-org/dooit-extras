from dooit.ui.api import DooitAPI


def toggle_workspaces(api: DooitAPI):
    def wrapper():
        """Toggles the visibility of the workspaces tree"""
        workspace_switcher = api.app.query_one("#workspace_switcher")
        todo_switcher = api.app.query_one("#todo_switcher")

        if workspace_switcher.display:
            workspace_switcher.display = False
            todo_switcher.styles.column_span = 2
            api.switch_focus()
        else:
            workspace_switcher.display = True
            todo_switcher.styles.column_span = 1
            api.app.workspace_tree.focus()

    return wrapper
