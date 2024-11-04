# Toggle Workspaces

This script can toggle the view for workspaces tree

You can bind it to a keybinding and use that

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The dooit api object                                                                     |

Example:

```py
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup
from dooit_extras.scripts import toggle_workspaces

@subscribe(Startup)
def setup(api: DooitAPI, _):
    api.keys.set("<ctrl+b>", toggle_workspaces(api))
```

Preview:

<video controls="controls" src="./previews/toggle_workspaces.mp4" />
