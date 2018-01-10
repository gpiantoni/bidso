from pathlib import Path
from re import search


def read_tsv(filename):
    filename = Path(filename)
    with filename.open() as f:
        hdr = f.readline()
        tsv = []
        for l in f:
            d = {k.strip(): v.strip() for k, v in zip(hdr.split('\t'), l.split('\t'))}
            tsv.append(d)
    return tsv


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


def mkdir_task(base_path, task):

    feat_path = base_path / ('sub-' + task.subject)
    feat_path.mkdir(exist_ok=True)
    if hasattr(task, 'session') and task.session is not None:  # hasattr for pybids, isnone for bidso
        feat_path = feat_path / ('ses-' + task.session)
        feat_path.mkdir(exist_ok=True)

    feat_path = feat_path / task.modality
    feat_path.mkdir(exist_ok=True)

    return feat_path


def _match(filename, pattern):
    m = search(pattern, filename.stem)
    if m is None:
        return m
    else:
        return m.group(1)
