from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup
from dooit_extras.formatters import *
from dooit_extras.bar_widgets import *
from dooit_extras.scripts import *

@subscribe(Startup)
def setup_formatters(api: DooitAPI, _):
    fmt = api.formatter

    fmt.workspaces.description.add(description_children_count())
    fmt.todos.description.add(todo_description_progress())
