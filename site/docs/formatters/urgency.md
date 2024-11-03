# Urgency Formatters

## Urgency Icons

This formatter shows different icons based on the urgency level of the todo

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| icons         |  `{}`               | A dictionary with icon for respective urgency levels                                     |
| colors        |  `{}`               | A dictionary with styles for respective urgency levels                                   |

Example icons:

Example icons:

```py
{1: "󰲠", 2: "󰲢", 3: "󰲤", 4: "1"}
```

Example colors:

```py
{1: theme.green, 2: theme.yellow, 3: theme.orange, 4: theme.red}
```

### Usage:

```python

from dooit_extras.formatters import urgency_icons
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.urgency.add(urgency_icons())
    # ...
```