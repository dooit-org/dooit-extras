from dooit.api.theme import DooitThemeBase


class Dracula(DooitThemeBase):
    _name = "dooit-dracula"

    background1: str = "#282a36"  # Darkest
    background2: str = "#44475a"  # Lighter
    background3: str = "#5f637e"  # Lightest

    # foreground colors
    foreground1: str = "#cccccc"  # Darkest
    foreground2: str = "#e6e6e6"  # Lighter
    foreground3: str = "#f8f8f2"  # Lightest

    # other colors
    red: str = "#ff5555"
    orange: str = "#ffb86c"
    yellow: str = "#f1fa8c"
    green: str = "#50fa7b"
    blue: str = "#8be9fd"
    purple: str = "#bd93f9"
    magenta: str = "#ff79c6"
    cyan: str = "#8be9fd"

    # accent colors
    primary: str = purple
    secondary: str = cyan
