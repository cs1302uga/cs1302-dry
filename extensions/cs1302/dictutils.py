from functools import reduce
from typing import Any


def dict_get(d: dict, *keys) -> Any:
    """TODO"""
    return reduce(dict.get, (d, *keys))


def dict_read(d: dict, path: str) -> Any:
    """TODO"""
    keys = map(str.strip, path.split("."))
    return dict_get(d, *keys)
