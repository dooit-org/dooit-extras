from dooit.api import Todo
from dooit.ui.api import DooitAPI, subscribe
from dooit.ui.api.events import Startup
from dooit.api.theme import DooitThemeBase
from dooit.ui.api.widgets import TodoWidget
from rich.style import Style
from dooit_extras.formatters import *
from dooit_extras.bar_widgets import *
from dooit_extras.scripts import *
from rich.text import Text


class Everforest(DooitThemeBase):
    _name: str = "dooit-everforest"

    # background colors
    background1: str = "#2b3339"  # Darkest
    background2: str = "#323d43"  # Lighter
    background3: str = "#3a454a"  # Lightest

    # foreground colors
    foreground1: str = "#d3c6aa"  # Darkest
    foreground2: str = "#e9e8d2"  # Lighter
    foreground3: str = "#fdf6e3"  # Lightest

    # other colors
    red: str = "#e67e80"  # Red
    orange: str = "#e69875"  # Orange
    yellow: str = "#dbbc7f"  # Yellow
    green: str = "#a7c080"  # Green
    blue: str = "#7fbbb3"  # Blue
    purple: str = "#d699b6"  # Purple
    magenta: str = "#d699b6"  # Magenta (same as purple in Everforest)
    cyan: str = "#83c092"  # Cyan

    # accent colors
    primary: str = cyan
    secondary: str = green


@subscribe(Startup)
def setup_colorscheme(api: DooitAPI, _):
    api.css.set_theme(Everforest)


@subscribe(Startup)
def setup_formatters(api: DooitAPI, _):
    fmt = api.formatter
    theme = api.vars.theme

    # ------- WORKSPACES -------
    format = Text(" ({}) ", style=theme.primary).markup
    fmt.workspaces.description.add(description_children_count(format))

    # --------- TODOS ---------
    # status formatter
    fmt.todos.status.add(status_icons(completed="󱓻 ", pending="󱓼 ", overdue="󱓼 "))

    # urgency formatte
    u_icons = {1: "  󰯬", 2: "  󰯯", 3: "  󰯲", 4: "  󰯵"}
    fmt.todos.urgency.add(urgency_icons(icons=u_icons))

    # due formatter
    fmt.todos.due.add(due_casual_format())
    fmt.todos.due.add(due_icon(completed="󰐅 ", pending="󱢗 ", overdue="󱐚 "))

    # effort formatter
    fmt.todos.effort.add(effort_icon(icon="󱠇 "))

    # description formatter
    format = Text("  {completed_count}/{total_count}", style=theme.green).markup
    fmt.todos.description.add(todo_description_progress(fmt=format))
    fmt.todos.description.add(description_highlight_tags(fmt="󰌪 {}"))
    fmt.todos.description.add(description_strike_completed())


@subscribe(Startup)
def setup_layout(api: DooitAPI, _):
    api.layouts.todo_layout = [
        TodoWidget.status,
        TodoWidget.description,
        TodoWidget.due,
    ]


@subscribe(Startup)
def setup_bar(api: DooitAPI, _):
    theme = api.vars.theme
    mode_aliases = {"NORMAL": "NOR", "INSERT": "INS"}

    widgets = [
        Mode(api, mode_aliases, fmt = " 󰌪 {}"),
        Powerline.right_rounded(api, fg=theme.primary),
        Spacer(api, width=0),
        Powerline.left_rounded(api, fg=theme.primary),
        Ticker(api, fmt=" 󱎫 {} "),
        Powerline.left_rounded(api, fg=theme.yellow, bg = theme.primary),
        Clock(api, format = "%H:%M", fmt=" 󰥔 {} ", bg = theme.yellow),
    ]
    api.bar.set(widgets)


@subscribe(Startup)
def setup_dashboard(api: DooitAPI, _):
    theme = api.vars.theme

    ascii_art = r"""
                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                             
          X            Help, I can't finish! 
          X          -                                      .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                 _____|_____
    .a################aa.                              \  DOOIT  /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

    ascii_art = Text(ascii_art, style=theme.primary)
    ascii_art.highlight_words([" Help, I can't finish! "], style="reverse")
    ascii_art.highlight_words([" DOOIT "], style=theme.secondary)

    header = Text(
        "Welcome again to your daily life, piled with unfinished tasks!",
        style=Style(color=theme.secondary, bold=True, italic=True),
    )

    items = [
        header,
        ascii_art,
        "",
        "",
        Text("Will you finish your tasks today?", style=theme.secondary),
    ]
    api.dashboard.set(items)


@subscribe(Startup)
def additional_setup(api: DooitAPI, _):
    dim_unfocused(api, "60%")
