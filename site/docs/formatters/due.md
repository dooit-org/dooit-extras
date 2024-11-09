# Due Formatters

## Casual Format

This widget shows the date in a simple format

Eg: Instead of the default `yyyy-mm-dd`, it'll show in the format: \
`{Mon} {day} ['year(optional)] + <HH:MM if present>`

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| fmt           |  `"{}"`             | The custom format for showing the value                                                  |

```python

from dooit_extras.formatters import due_casual_format
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.due.add(due_casual_format())
    # ...
```


## Danger Today

This formatter shows a bold red `Today` text when the todo is due on the same day

```python

from dooit_extras.formatters import due_danger_today
from dooit.ui.api.events import subscribe, Startup

| Param|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| fmt           |  `"{}"`             | The custom format for showing the value                                                  |

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.due.add(due_danger_today())
    # ...
```

## Due Icon

This formatter shows due icons based on status.

| Param       |<div style="width: 100px">Default</div> | Description                                      |
|-------------|:--------------------------------------:|:-------------------------------------------------|
| completed   | <span class="nerd-icon">󰃯</span>       | Icon for completed todo                          |
| pending     | <span class="nerd-icon">󰃰</span>       | Icon for pending todo                            |
| overdue     | <span class="nerd-icon"></span>       |  Icon for overdue todo                           |


```python

from dooit_extras.formatters import due_icon
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    # ...
    api.formatter.todos.due.add(due_icon())
    # ...
```
