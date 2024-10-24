# Ticker

A widget to show a timer

| Key|<div style="width: 100px">Default</div> |Description|
| ------------ | :----------------:  | :----------------------------------------------------------------------------------------|
|api           |                     | The api object provided within the function                                              |
|resume_key    | `"s"`               | Key to `start` or `resume` the timer to pause                                            |
|stop_key      | `"S"`               | Key to `stop/pause` the timer. Stopping again will `reset` the timer                     |
|paused_text   | `"Paused"`          | Text to show when the timer is paused                                                    |
|default_text  | `"No Timers"`       | Default text to show for the timer widget. When the timer is reset, this text will show as well|
|fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
|fg            | `theme.foreground_1`| Color to show the text in, defaults to `theme.foreground_1` or `white` based on theme    |
|bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |

## Usage

```python
from dooit_extras.bar_widgets import Ticker
from dooit.ui.api.events import subscribe, Startup

@subscribe(Startup)
def setup(api, _):
    api.bar.set( 
        [
            # ....
            Ticker(
                api,
                resume_key = "s",
                stop_key = "S",
                paused_text = "Paused",
                default_text = "No Timers",
            )
            # ....
        ]
    )
```
