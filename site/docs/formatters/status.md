# Status Formatters

## Status Icons

This formatter shows different icons based on the current status of the todo

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| icons         |  `{}`               | A dictionary with icon for respective statuses                                           |
| colors        |  `{}`               | A dictionary with styles for respective statuses                                         |

Example icons:

```py
{"completed": "x", "pending": "o", "overdue": "!"}
```

Example colors:

```py
{"completed": theme.green, "pending": theme.yellow, "overdue": theme.red}
```


::: tip INFO
By default, icons for completed, pending and overdue are `x`, `o` and `!` respectively \
Similiarly, the colors are theme versions of `green`, `yellow` and `red`

So if any of the keys are missing, it'll use the default icons
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


