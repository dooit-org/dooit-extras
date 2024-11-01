from dooit.api.theme import DooitThemeBase


class Material(DooitThemeBase):
    _name = "dooit-material"

    background1: str = "#263238"  # Darkest
    background2: str = "#2E3C43"  # Lighter
    background3: str = "#314549"  # Lightest

    # foreground colors
    foreground1: str = "#90A4AE"  # Darkest
    foreground2: str = "#B0BEC5"  # Lighter
    foreground3: str = "#EEFFFF"  # Lightest

    # other colors
    red: str = "#F07178"
    orange: str = "#F78C6C"
    yellow: str = "#FFCB6B"
    green: str = "#C3E88D"
    blue: str = "#82AAFF"
    purple: str = "#C792EA"
    magenta: str = "#FF5370"
    cyan: str = "#89DDFF"

    # accent colors
    primary: str = blue
    secondary: str = cyan
