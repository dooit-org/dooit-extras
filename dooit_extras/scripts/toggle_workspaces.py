from dooit.ui.api import DooitAPI

CSS = """
#workspace_switcher {
    display: none;
}

#todo_switcher {
    column-span: 2;
}
"""

CSS_ID = "toggle_workspaces"

def toggle_workspaces(api: DooitAPI):
    def wrapper():
        if api.css.is_active(CSS_ID):
            api.css.unject_css(CSS_ID)
            api.app.workspace_tree.focus()

        else:
            if api.app.workspace_tree.has_focus:
                api.switch_focus()

            api.css.inject_css(CSS, CSS_ID)
    return wrapper
