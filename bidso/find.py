from pathlib import Path


def find_root(filename, pattern='sub-'):
    """Pattern: 'sub-', 'ses-'"""
    if not isinstance(filename, Path):  # f.e. if it's Task or file_XXX
        filename = filename.filename

    if filename.is_dir() and filename.stem.startswith(pattern):
        return filename
    else:
        return find_root(filename.parent)


def find_modality(dir_name, modality='anat'):
    """TODO: it should not go deeper than subject"""
    if not isinstance(dir_name, Path):  # f.e. if it's Task or file_XXX
        dir_name = dir_name.filename.parent

    for one_dir in dir_name.rglob('*'):
        print(one_dir)
        if one_dir.name == modality:
            return one_dir
    else:
        return find_modality(dir_name.parent)
