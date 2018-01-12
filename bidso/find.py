from pathlib import Path


def find_root(filename, pattern='sub-'):
    """Pattern: 'sub-', 'ses-'"""
    if not isinstance(filename, Path):  # f.e. if it's Task or file_XXX
        filename = filename.filename

    if filename.is_dir() and filename.stem.startswith(pattern):
        return filename
    else:
        return find_root(filename.parent)


def find_nearest(dir_name, pattern='anat'):
    """TODO: it should not go deeper than subject

    TODO: how to handle multiple results
    """
    if not isinstance(dir_name, Path):  # f.e. if it's Task or file_XXX
        dir_name = dir_name.filename.parent

    try:
        return next(dir_name.rglob(pattern))

    except StopIteration:
        return find_nearest(dir_name.parent, pattern)
