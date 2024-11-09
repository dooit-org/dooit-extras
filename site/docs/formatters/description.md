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

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| color         |  `None`             | The color to use for highlighting URLs. If not provided, uses the theme's primary color   |

```python

from dooit_extras.formatters import description_highlight_link
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.workspaces.description.add(description_highlight_link())
    api.formatter.todos.description.add(description_highlight_link())
    # ...
```

## Highlight Tags

This formatter highlights the tags(words starting with `@`) present in the description 

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| color         |  `""`               | The color/style to use for highlighting the tags, Defaults to theme's primary color      |
| fmt           |<span class="nerd-icon">" {}"</span>| The format to use to show the tags                                       |

```python

from dooit_extras.formatters import description_highlight_tags
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.workspaces.description.add(description_highlight_tags())
    api.formatter.todos.description.add(description_highlight_tags())
    # ...
```


## Strike Completed

This formatter strikes the todos which are completed, and optionally dimmify them

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| dim           |  `True`             | Whether to dim the todo description                                                      |

```python

from dooit_extras.formatters import todo_description_progress
from dooit.ui.api.events import subscribe, Startup


@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.workspaces.description.add(description_strike_completed(dim = True))
    api.formatter.todos.description.add(description_strike_completed(dim = True))
    # ...
```

## Todo Progress

Formatter to show the progress of a current todo with subtasks

***Parameters***:

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| fmt           |  `" ({completed_percent}%)"`  | The format of the progress                                                    |


Options available for `fmt` parameters are:

|<div style="width: 100px">Name</div> |Description|
| :----------------:    | :----------------------------------------------------------------------------------------|
|  completed_percent    | The current progress in percentage (1-100)                                               |
|  remaining_percent    | The remaining progress in percentage (1-100)                                             |
|  completed_count      | The number of subtask completed                                                          |
|  remaining_count      | The number of subtask not completed                                                      |
|  total_count          | The total number of subtask the todo has                                                 |

```python

from dooit_extras.formatters import description_strike_completed
from dooit.ui.api.events import subscribe, Startup


@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.description.add(todo_description_progress())
    # ...
```
