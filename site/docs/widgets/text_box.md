# Text Box

A widget to show static Text

::: tip
Check out [Custom](/widgets/custom) if you want dynamic texts
:::

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| text          |                     | Text to show in the widget                                                               |
| fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
| fg            | `theme.foreground1`| Color to show the text in, defaults to `theme.foreground1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

## Usage

```python
from dooit_extras.bar_widgets import TextBox
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    api.bar.set( 
        [
            # ....
            TextBox(api, text = "Your text here!"),
            # ....
        ]
    )
```
