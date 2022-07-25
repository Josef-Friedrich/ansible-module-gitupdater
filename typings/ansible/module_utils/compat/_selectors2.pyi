"""
This type stub file was generated by pyright.
"""

import select
import sys

from ansible.module_utils.common._collections_compat import Mapping

__author__ = ...
__email__ = ...
__version__ = ...
__license__ = ...
__all__ = [
    "EVENT_READ",
    "EVENT_WRITE",
    "SelectorError",
    "SelectorKey",
    "DefaultSelector",
]
EVENT_READ = ...
EVENT_WRITE = ...
HAS_SELECT = ...
_SYSCALL_SENTINEL = ...

class SelectorError(Exception):
    def __init__(self, errcode) -> None: ...
    def __repr__(self): ...
    def __str__(self) -> str: ...

if sys.version_info >= (3, 5): ...
else: ...
SelectorKey = ...

class _SelectorMapping(Mapping):
    """Mapping of file objects to selector keys"""

    def __init__(self, selector) -> None: ...
    def __len__(self): ...
    def __getitem__(self, fileobj): ...
    def __iter__(self): ...

class BaseSelector:
    """Abstract Selector class

    A selector supports registering file objects to be monitored
    for specific I/O events.

    A file object is a file descriptor or any object with a
    `fileno()` method. An arbitrary object can be attached to the
    file object which can be used for example to store context info,
    a callback, etc.

    A selector can use various implementations (select(), poll(), epoll(),
    and kqueue()) depending on the platform. The 'DefaultSelector' class uses
    the most efficient implementation for the current platform.
    """

    def __init__(self) -> None: ...
    def register(self, fileobj, events, data=...):  # -> SelectorKey:
        """Register a file object for a set of events to monitor."""
        ...
    def unregister(self, fileobj):
        """Unregister a file object from being monitored."""
        ...
    def modify(self, fileobj, events, data=...):  # -> SelectorKey:
        """Change a registered file object monitored events and data."""
        ...
    def select(self, timeout=...):
        """Perform the actual selection until some monitored file objects
        are ready or the timeout expires."""
        ...
    def close(self):  # -> None:
        """Close the selector. This must be called to ensure that all
        underlying resources are freed."""
        ...
    def get_key(self, fileobj):
        """Return the key associated with a registered file object."""
        ...
    def get_map(self):  # -> _SelectorMapping | None:
        """Return a mapping of file objects to selector keys"""
        ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

if hasattr(select, "select"):
    class SelectSelector(BaseSelector):
        """Select-based selector."""

        def __init__(self) -> None: ...
        def register(self, fileobj, events, data=...): ...
        def unregister(self, fileobj): ...
        def select(self, timeout=...): ...

if hasattr(select, "poll"):
    class PollSelector(BaseSelector):
        """Poll-based selector"""

        def __init__(self) -> None: ...
        def register(self, fileobj, events, data=...): ...
        def unregister(self, fileobj): ...
        def select(self, timeout=...): ...

if hasattr(select, "epoll"):
    class EpollSelector(BaseSelector):
        """Epoll-based selector"""

        def __init__(self) -> None: ...
        def fileno(self): ...
        def register(self, fileobj, events, data=...): ...
        def unregister(self, fileobj): ...
        def select(self, timeout=...): ...
        def close(self): ...

if hasattr(select, "devpoll"):
    class DevpollSelector(BaseSelector):
        """Solaris /dev/poll selector."""

        def __init__(self) -> None: ...
        def fileno(self): ...
        def register(self, fileobj, events, data=...): ...
        def unregister(self, fileobj): ...
        def select(self, timeout=...): ...
        def close(self): ...

if hasattr(select, "kqueue"):
    class KqueueSelector(BaseSelector):
        """Kqueue / Kevent-based selector"""

        def __init__(self) -> None: ...
        def fileno(self): ...
        def register(self, fileobj, events, data=...): ...
        def unregister(self, fileobj): ...
        def select(self, timeout=...): ...
        def close(self): ...

if "KqueueSelector" in globals():
    DefaultSelector = ...
else:
    DefaultSelector = ...