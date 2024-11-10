from time import time
from dooit.ui.api import DooitAPI, timer
from .text_poller import Custom


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
        self._start_flag = False

    def current_count(self) -> float:
        if self._running and self._start_time:
            return self._elapsed_time + (time() - self._start_time)
        return self._elapsed_time

    def format_hms(self):
        """Converts the current count to h m s format."""

        total_seconds = int(self.current_count())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        parts.append(f"{seconds}s")

        return " ".join(parts)


def get_ticker_wrapper(counter: Counter, paused_text: str, default_text: str):
    @timer(0.2)
    def get_ticker(*_) -> str:
        if counter._start_flag:
            if counter.is_paused():
                return paused_text
            else:
                return counter.format_hms()
        else:
            return default_text

    return get_ticker


class Ticker(Custom):
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
            api=api,
            function=get_ticker_wrapper(self.counter, paused_text, default_text),
            width=None,
            fmt=fmt,
            fg=fg,
            bg=bg,
        )

        # set keybinds
        self.api.keys.set(resume_key, self.counter.start)
        self.api.keys.set(stop_key, self.counter.stop)
