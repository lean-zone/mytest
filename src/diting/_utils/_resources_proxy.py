from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `diting.resources` module.

    This is used so that we can lazily import `diting.resources` only when
    needed *and* so that users can just import `diting` and reference `diting.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("diting.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
