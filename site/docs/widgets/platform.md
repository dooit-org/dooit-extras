# Platform

A widget to show the current OS platform!

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| icon          | `True`              | Whether to show the icon of the OS or not.                                               |
| fg            | `theme.foreground_1`| Color to show the text in, defaults to `theme.foreground_1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

::: tip
If your system does not have an icon, feel free to [open an issue](https://github.com/dooit-org/dooit-extras/issues/new) :D
:::

## Usage

```python
from dooit_extras.bar_widgets import Platform

api.bar.set( 
    [
        # ....
        Platform(api),
        # ....
    ]
)
```
