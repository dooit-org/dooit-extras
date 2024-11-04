from dooit.ui.api import DooitAPI


def dim_unfocused(api: DooitAPI, opacity: str = "50%"):
    """Dimmify unfocused tree"""

    CSS = f"""\
    ModelTree {{
        opacity: {opacity};

        &:focus {{ 
           opacity: 1;
       }}
    }}
    """

    api.css.inject_css(CSS)
    api.app.refresh_css()  # quick refresh
