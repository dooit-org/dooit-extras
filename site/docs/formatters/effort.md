# Effort Formatters

## Effort Icon

This formatter shows an icon for todos that have effort enabled

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| icon          |  <span class="nerd-icon">󰈸</span>       | The icon to show for todos with effort                                                   |
| color         |  `None`             | The color to use for the icon. If not provided, uses the theme's orange color            |
| show_on_zero  |  `True`             | Whether to show the icon when effort is 0                                                |

```python

from dooit_extras.formatters import effort_icon
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup

@subscribe(Startup)
def setup(api: DooitAPI, _):
    # ...
    api.formatter.todos.effort.add(effort_icon())
    # ...
```