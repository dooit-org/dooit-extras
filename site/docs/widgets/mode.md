# Mode

A widget to show current mode (`NORMAL/INSERT`) of the app

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------: | :----------------------------------------------------------------------------------------|
| api           |                    | The api object provided within the function                                              |
| format_normal | `"NORMAL"`         | Specify how `normal` mode should be displayed in text                                    |
| format_insert | `"INSERT"`         | Specify how `insert` mode should be displayed in text                                    |
| fmt           | `" {} "`           | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
| fg            | `theme.background1`| Color to show the text in, defaults to `theme.background1` or `dark` based on theme      |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme |

```python
from dooit_extras.bar_widgets import Mode
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    theme = api.vars.theme

    api.bar.set( 
        [
            # ....
            Mode(api)
            # ....
        ]
    )
```
