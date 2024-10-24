# Text Poller

A widget which which takes in a custom function to display text

| Key|<div style="width: 100px">Default</div> |Description|
| ------------- | :----------------:  | :----------------------------------------------------------------------------------------|
| api           |                     | The api object provided within the function                                              |
| function      |                     | Function top poll the value from, events and intervals can be set with  [@subscribe](https://www.google.com)   |
| fmt           | `" {} "`            | Specify how the text should be formatted, `{}` represents the value that'll be displayed |
| fg            | `theme.foreground_1`| Color to show the text in, defaults to `theme.foreground_1` or `white` based on theme    |
| bg            | `theme.primary`     | Color to show the background in, defaults to `theme.primary` or `accent` based on theme  |
