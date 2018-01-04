def replace_extension(filename, suffix):
    if isinstance(filename, str):
        return filename.split('.')[0] + suffix
    else:
        return filename.parent / (filename.name.split('.')[0] + suffix)


def add_underscore(filename, suffix):
    if isinstance(filename, str):
        return filename + '_' + suffix
    else:
        return filename.parent / (filename.name + '_' + suffix)


def replace_underscore(filename, suffix):
    if isinstance(filename, str):
        return '_'.join(filename.split('_')[:-1] + [suffix, ])
    else:
        return filename.parent / ('_'.join(filename.name.split('_')[:-1] + [suffix, ]))


def remove_underscore(filename):
    if isinstance(filename, str):
        return '_'.join(filename.split('_')[:-1])
    else:
        return filename.parent / ('_'.join(filename.name.split('_')[:-1]))


def find_root(filename, pattern='sub-'):
    """Pattern: 'sub-', 'ses-'"""

    if filename.is_dir() and filename.stem.startswith(pattern):
        return filename
    else:
        return find_root(filename.parent)
