from ._get_path import get_path

# All functions imported are import from root from this package
# because of to avoid cyclic import and better import name.
__all__ = [get_path]
