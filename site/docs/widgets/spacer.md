# Spacer

A widget to add padding between widgets!

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| width         |                     | The width of the spacer, set `0` to expand to full width                                 |
| fg            | `theme.foreground_1`| Color to show the text in, defaults to `theme.foreground_1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

## Usage

```python
from dooit_extras.bar_widgets import Spacer
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    api.bar.set( 
        [
            # ....
            Spacer(api, width = 0), # takes all the space
            Spacer(api, width = 20), # takes 20 blocks worth of space
            # ....
        ]
    )
```
