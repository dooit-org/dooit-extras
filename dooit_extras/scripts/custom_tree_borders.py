from typing import Literal
from dooit.ui.api import DooitAPI

BorderKind = Literal[
    "ascii",
    "blank",
    "dashed",
    "double",
    "heavy",
    "hidden" "hkey",
    "inner",
    "outer",
    "panel",
    "round",
    "solid",
    "tall",
    "thick",
    "vkey",
    "wide",
]


def custom_tree_borders(
    api: DooitAPI,
    focus_border: BorderKind,
    dim_border: BorderKind,
):
    """Customize tree borders"""
    CSS = f"""\
    ModelTree {{
        border: {dim_border} $background3;

        &:focus {{ 
           border: {focus_border} $primary;
       }}
    }}
    """

    api.css.inject_css(CSS)
    api.app.refresh_css()  # quick refresh
