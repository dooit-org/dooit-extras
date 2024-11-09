# Status Formatters

## Status Icons

This formatter shows different icons based on the current status of the todo

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| completed     |  `"x"`               | The icon to show when status is `completed`                                             |
| pending       |  `"o"`               | The icon to show when status is `pending`                                               |
| overdue       |  `"!"`               | The icon to show when status is `overdue`                                               |


::: tip INFO
By default, the colors are theme versions of `green`, `yellow` and `red`
:::

### Usage:

```python

from dooit_extras.formatters import status_icons
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.status.add(status_icons(...))
    # ...
```


