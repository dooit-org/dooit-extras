# Custom

A widget which which takes in a custom function to display text

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| function      |                     | Function top poll the value from, events and intervals can be set with  [@subscribe](https://www.google.com) and [@timer](https://www.google.com)   |
| fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
| fg            | `theme.foreground1`| Color to show the text in, defaults to `theme.foreground1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

```python
from dooit_extras.bar_widgets import Custom
from dooit.ui.api.events import subscribe, timer, Startup, TodoEvent
from dooit.ui.api import DooitAPI

@subscribe(TodoEvent)
def alert_todo_event(api: DooitAPI, event: TodoEvent):
    # ...

@timer(1)
def my_timer(api: DooitAPI, _):
    # ...

@subscribe(Startup)
def setup(api, _):
    api.bar.set( 
        [
            # ....
            Custom(api, function = alert_todo_event),
            Custom(api, function = my_timer),
            # ....
        ]
    )
```
