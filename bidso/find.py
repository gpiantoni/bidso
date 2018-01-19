from warnings import warn
from logging import getLogger

lg = getLogger(__name__)


def find_root(filename, target='bids'):
    """Find base directory (root) for a filename.

    Parameters
    ----------
    filename : instance of Path
        search the root for this file
    target: str
        'bids' (the directory containing 'participants.tsv'), 'subject' (the
        directory starting with 'sub-'), 'session' (the directory starting with
        'ses-')

    Returns
    -------
    Path
        path of the target directory
    """
    lg.debug(f'Searching root in {filename}')
    if target == 'bids' and (filename / 'participants.tsv').exists():
        return filename
    elif filename.is_dir():
        pattern = target[:3] + '-'
        if filename.stem.startswith(pattern):
            return filename

    return find_root(filename.parent, target)


def find_nearest(filename, pattern=None, **kwargs):
    """Find nearest file matching some criteria.

    Parameters
    ----------
    filename : instance of Path
        search the root for this file
    pattern : str
        glob string for search criteria of the filename of interest (remember
        to include '*'). The pattern is passed directly to rglob.
    kwargs : dict


    Returns
    -------
    Path
        closest filename matching the pattern
    """
    lg.debug(f'Searching nearest in {filename}')

    if pattern is None:
        pattern = _generate_pattern(kwargs)

    if filename == find_root(filename):
        raise FileNotFoundError(f'Could not find file matchting {pattern} in {filename}')

    matches = list(filename.rglob(pattern))
    if len(matches) == 1:
        return matches[0]
    elif len(matches) == 0:
        return find_nearest(filename.parent, pattern)
    else:
        matches_str = '"\n\t"'.join(str(x) for x in matches)
        raise FileNotFoundError(f'Multiple files matching "{pattern}":\n\t"{matches_str}"')


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


