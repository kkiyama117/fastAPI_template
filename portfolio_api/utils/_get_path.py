import functools
import logging
import pathlib
from typing import Union

module_logger = logging.getLogger(__name__)
project_root = pathlib.Path(__file__).parent.parent.parent


@functools.singledispatch
def get_path(file_path: Union[str, pathlib.Path]) -> pathlib.Path:
    """Path object を取得
    strでも既にPathになっていても取得出来る
    Args:
        file_path (Union]): path of file
    Returns:
        path object of file at file_path
    Raises:
        ValueError: if `file_path` is not str or pathlib.Path
    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.
        >>> get_path("settings.json")
        Path("setting.json")
        >>> path=pathlib.Path("settings.json")
        >>> get_path(path)
        Path('setting.json')
    """
    raise ValueError(f"type of args {file_path} of path is incorrect")


@get_path.register(str)
def _get_path_from_str(file_path) -> pathlib.Path:
    return (project_root / file_path).resolve()


@get_path.register(pathlib.Path)
def _get_path_from_path(file_path) -> pathlib.Path:
    return file_path.resolve()
