# Mode

A widget to show current mode (`NORMAL/INSERT/...` etc) of the app

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------: | :----------------------------------------------------------------------------------------|
| api           |                    | The api object provided within the function                                              |
| mode_styles   | `{}`               | A dictionary of key/value with key as `mode name` and value is a `Style` object          |
| fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |

```python
from dooit_extras.bar_widgets import Mode

theme = api.vars.theme

mode_styles = {
    "NORMAL": theme.primary,
    "INSERT": theme.secondary,
}

api.bar.set( 
    [
        # ....
        Mode(api, mode_styles = mode_styles)
        # ....
    ]
)
```
