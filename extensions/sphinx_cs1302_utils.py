from typing import Any, Dict


def make_sub(name, value):
    """TODO."""
    return f".. |{name}| replace:: {value}"


def make_ref(name, url):
    """TODO."""
    return f".. _{name}: {url}"


def make_subref(name, title, url=""):
    """TODO."""
    return "\n".join(
        [
            make_sub(name, title),
            make_url(name, url),
        ]
    )


def setup(app) -> Dict[str, Any]:
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
