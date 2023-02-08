import tomllib

from cs1302.dictutils import dict_get, dict_read
from pathlib import Path


def load_pyproject(home: str | Path = Path(".")) -> dict:
    """Return a copy of `pyproject.toml` as a dictionary.

    Args:
        home: Path to the directory that contains `pyproject.toml`.

    Returns:
        A `dict` containing copies of the entries in `pyproject.toml`.
    """
    pyproject_file = Path(home) / "pyproject.toml"
    with open(pyproject_file, "rb") as pyproject:
        pyproject = tomllib.load(pyproject)
        return pyproject
