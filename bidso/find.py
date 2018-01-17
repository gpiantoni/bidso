from warnings import warn
from logging import getLogger

lg = getLogger(__name__)


def find_root(filename, target='bids'):
    """Target: 'bids', 'subject', 'session'
    """
    lg.debug(f'Searching root in {filename}')
    if target == 'bids' and (filename / 'participants.tsv').exists():
        return filename
    elif filename.is_dir():
        pattern = target[:3] + '-'
        if filename.stem.startswith(pattern):
            return filename

    return find_root(filename.parent, target)


def _generate_pattern(kwargs):
    pattern = ''
    for k, v in kwargs.items():
        if k == 'subject':
            pattern += 'sub-' + v
        elif k == 'session':
            pattern += 'ses-' + v
        elif k == 'run':
            pattern += 'run-' + v
        elif k == 'modality':
            pattern += '_' + v
        elif k == 'extension':
            pattern += v
            break  # extension is always the last one
        else:
            warn(f'Unrecognized type "{k}"')
            continue

        pattern += '*'

    return pattern


def find_nearest(dir_name, pattern=None, **kwargs):
    lg.debug(f'Searching nearest in {dir_name}')

    if pattern is None:
        pattern = _generate_pattern(kwargs)

    if dir_name == find_root(dir_name):
        raise FileNotFoundError(f'Could not find file matchting {pattern} in {dir_name}')

    matches = list(dir_name.rglob(pattern))
    if len(matches) == 1:
        return matches[0]
    elif len(matches) == 0:
        return find_nearest(dir_name.parent, pattern)
    else:
        matches_str = '"\n\t"'.join(str(x) for x in matches)
        raise FileNotFoundError(f'Multiple files matching "{pattern}":\n\t"{matches_str}"')
