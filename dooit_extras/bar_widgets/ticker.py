from time import time
from dooit.ui.api import DooitAPI
from dooit.ui.api.events import timer
from rich.text import Text
from rich.style import Style

from ._base import BarUtilWidgetBase


class Counter:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0
        self._running = False
        self._start_flag = False

    def start(self):
        """Starts the counter"""
        self._start_flag = True
        if not self._running:
            self._start_time = time()
            self._running = True

    def stop(self):
        """Stops the counter. Reset when already stopped"""
        if self._running and self._start_time:
            self._elapsed_time += time() - self._start_time
            self._start_time = None
            self._running = False
        else:
            self.reset()

    def is_paused(self):
        """Checks if the counter is currently paused."""
        return not self._running and self._start_flag

    def reset(self):
        self._start_time = None
        self._elapsed_time = 0
        self._running = False

    def current_count(self) -> int:
        if self._running and self._start_time:
            return int(self._elapsed_time + (time() - self._start_time))
        return int(self._elapsed_time)


def get_ticker_wrapper(counter: Counter, paused_text: str, default_text: str):
    @timer(1)
    def get_ticker(*_) -> str:
        if counter._start_flag:
            if counter.is_paused():
                return paused_text
            else:
                return str(counter.current_count())
        else:
            return default_text

    return get_ticker


class Ticker(BarUtilWidgetBase):
    def __init__(
        self,
        api: DooitAPI,
        resume_key: str = "s",
        stop_key: str = "S",
        paused_text: str = "Paused",
        default_text: str = "No Timers",
        fmt: str = " {} ",
        fg: str = "",
        bg: str = "",
    ) -> None:
        self.counter = Counter()

        super().__init__(
            func=get_ticker_wrapper(self.counter, paused_text, default_text),
            width=None,
            api=api,
            fmt=fmt,
        )

        self.fg = fg
        self.bg = bg

        # set keybinds
        self.api.keys.set(resume_key, self.counter.start)
        self.api.keys.set(stop_key, self.counter.stop)

    def render(self) -> Text:
        fg = self.fg or self.api.app.current_theme.background_1
        bg = self.bg or self.api.app.current_theme.primary
        style = Style(color=fg, bgcolor=bg)

        return self.render_text(style=style)
