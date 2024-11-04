# Custom Tree Borders

This script allows you to edit the border for workspaces and todo trees

Check out available border types [here](https://textual.textualize.io/styles/border/#all-border-types)

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The dooit api object                                                                     |
| focus_border  |                     | The border to use for the focused tree                                                   |
| dim_border    |                     | The border to use for the unfocused tree                                                 |

Example:

```py
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup
from dooit_extras.scripts import custom_tree_borders

@subscribe(Startup)
def setup(api: DooitAPI, _):
   custom_tree_borders(api, "panel", "panel")
```

Preview:

![Custom Tree Borders](./previews/custom_tree_borders.png)
