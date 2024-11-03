Recurrence Formatters

## Recurrence Icon

This formatter shows an icon for todos that have recurrence enabled

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| icon          |  <span class="nerd-icon">󰑖</span>       | The icon to show for recurring todos                                                     |
| color         |  `None`             | The color to use for the icon. If not provided, uses the theme's primary color           |


```python

from dooit_extras.formatters import recurrence_icon
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup

@subscribe(Startup)
def setup(api: DooitAPI, _):
    # ...
    api.formatter.todos.recurrence.add(recurrence_icon())
    # ...
```