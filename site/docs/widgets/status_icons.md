# StatusIcons

A widget to display count of `completed`, `pending` and `overdue` todos for selected workspace

| Key            | Default                              | Description                                                                   |
|----------------|:------------------------------------:|-------------------------------------------------------------------------------|
| api            |                                      | The `api` object provided within the function.                                |
| completed_icon | <span class="nerd-icon"></span>  | Icon to represent completed tasks.                                               |
| pending_icon   | <span class="nerd-icon"></span>  | Icon to represent pending tasks.                                                 |
| overdue_icon   | <span class="nerd-icon"></span>  | Icon to represent overdue tasks.                                                 |
| fmt            | `" {} "`                          | Format for displaying text, `{}` represents the value displayed.                 |
| bg             | `theme.background3`          | Background color for the widget, defaults to `theme.background3` or a specified color.|

## Usage

```python
from dooit_extras.bar_widgets import StatusIcons
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    api.bar.set(
        [
            # ....
            StatusIcons(api),
            # ....
        ]
    )
```

