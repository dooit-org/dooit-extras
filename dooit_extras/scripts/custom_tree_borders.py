from typing import Literal, Tuple
from dooit.ui.api import DooitAPI
from dooit.ui.widgets import ModelTree
from rich.style import StyleType

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
    focus_border: Tuple[BorderKind, StyleType],
    dim_border: Tuple[BorderKind, StyleType],
):
    """Customize tree borders"""
    CSS = f"""\
    ModelTree {{
        border: {dim_border[0]} {dim_border[1]};

        &:focus {{ 
           border: {focus_border[0]} {focus_border[1]};
       }}
    }}
    """

    api.css.inject_css(CSS)
