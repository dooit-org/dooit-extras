from ..widget import BarUtilWidgetBase
from dooit.ui.api import DooitAPI
from dooit.ui.api.events import subscribe
from dooit.ui.events import ModeChanged


@subscribe(ModeChanged)
def get_mode(api: DooitAPI, _: ModeChanged):
    return api.app._mode


class Mode(BarUtilWidgetBase):
    """
    Mode Bar Widget to show mode
    """

    def __init___(
        self,
        text_left: str = " ",
        text_right: str = " ",
        fg: str = "black",
        bg: str = "white",
        reverse_pads: bool = True,
    ) -> None:
        super().__init__(
            get_mode,
            width=None,
            text_left=text_left,
            text_right=text_right,
            fg=fg,
            bg=bg,
            reverse_pads=reverse_pads,
        )
