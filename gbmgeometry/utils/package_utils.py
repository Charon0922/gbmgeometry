try:
    # Preferred: Python 3.9+ importlib.resources.files API
    from importlib.resources import files as _ir_files
except Exception:
    try:
        # Backport for older Pythons
        from importlib_resources import files as _ir_files
    except Exception:
        _ir_files = None

import os
from shutil import copyfile


def get_path_of_data_file(data_file):
    path = get_path_of_data_dir()
    file_path = os.path.join(path, data_file)
    return file_path


def get_path_of_data_dir():
    """Return the filesystem path to the package data directory.

    Uses importlib.resources.files when available; falls back to
    pkg_resources.resource_filename if necessary.
    """
    if _ir_files is not None:
        data_dir = _ir_files("gbmgeometry").joinpath("data")
        # Traversable objects can be converted to a string path
        try:
            return str(data_dir)
        except Exception:
            pass

    # Fallback: try pkg_resources if importlib.resources is not available
    try:
        import pkg_resources

        return pkg_resources.resource_filename("gbmgeometry", "data")
    except Exception:
        # As a last resort return a relative path inside the package
        return os.path.join(os.path.dirname(__file__), os.pardir, "data")
