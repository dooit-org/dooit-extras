# Toggle Workspaces

This script can toggle the view for workspaces tree

You can bind it to a keybinding and use that

Example:

```py
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup

@subscribe(Startup)
def setup(api: DooitAPI, _):
    api.keys.set("<ctrl+b>", toggle_workspaces(api))
```
