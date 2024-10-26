# Description Formatters

## Children Count

This formatter shows the count of children present in a given `Todo`/`Workspace`

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| fmt           |  `" ({}) "`         | The format for showing the children                                                      |

```python

from dooit_extras.formatters import description_children_count
from dooit.ui.api.events import subscribe, Startup


@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.workspaces.description.add(description_children_count(fmt = "..."))
    api.formatter.todos.description.add(description_children_count(fmt = "..."))
    # ...
```


## Highlight Link

This formatter highlights any url present within the description with theme accent

### Usage:

```python

from dooit_extras.formatters import description_highlight_link
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.workspaces.description.add(description_highlight_link)
    api.formatter.todos.description.add(description_highlight_link)
    # ...
```


## Strike Completed

This idget strikes the todos which are completed, and optionally dimmify them

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| dim           |  `True`             | Whether to dim the todo description                                                      |

```python

from dooit_extras.formatters import description_strike_completed
from dooit.ui.api.events import subscribe, Startup


@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.workspaces.description.add(description_strike_completed(dim = True))
    api.formatter.todos.description.add(description_strike_completed(dim = True))
    # ...
```
