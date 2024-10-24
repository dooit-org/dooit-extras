# Workspace Progress

A widget to show current completion progress in percentage for a workspace

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
| fg            | `theme.foreground_1`| Color to show the text in, defaults to `theme.foreground_1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

## Usage

```python
from dooit_extras.bar_widgets import WorkspaceProgress
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    api.bar.set( 
        [
            # ....
            WorkspaceProgress(api),
            # ....
        ]
    )
```
