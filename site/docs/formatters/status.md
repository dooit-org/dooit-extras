# Status Formatters

## Status Icons

This widget modifies status icon to show customized icons

Eg: Instead of the default `yyyy-mm-dd`, it'll show in the format: \
`{Mon} {day} ['year(optional)]`

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| icons         |  `{}`               | The format for showing the children                                                      |
| colors        |  `{}`               | The format for showing the children                                                      |
| fmt           |  `"{}"`         | The format for showing the children                                                      |

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


