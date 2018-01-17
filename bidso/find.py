from pathlib import Path


def find_root(filename, pattern='sub-'):
    """Pattern: 'sub-', 'ses-'"""
    if not isinstance(filename, Path):  # f.e. if it's Task or file_XXX
        filename = filename.filename

    if filename.is_dir() and filename.stem.startswith(pattern):
        return filename
    else:
        return find_root(filename.parent)



def _generate_pattern(kwargs):
    pattern = ''
    for k, v in kwargs.items():
        if k == 'subject':
            pattern += 'sub-' + v 
        elif k == 'session':
            pattern += 'ses-' + v
        elif k == 'run':
            pattern += 'run-' + v
        elif k == 'extension': 
            pattern += v
            break  # extension is always the last one
        else:
            print(f'Unrecognized type "{k}"')
            continue

        pattern += '*'
        
    return pattern


def find_nearest(dir_name, pattern=None, **kwargs):
    """TODO: it should not go deeper than subject

    TODO: how to handle multiple results
    """
    if pattern is None:
        pattern = _generate_pattern(kwargs)    
    
    if dir_name == find_root(filename).parent:
        raise FileNotFoundError(f'Could not find file matchting {pattern} in {dir_name}')
    
    
    if not isinstance(dir_name, Path):  # f.e. if it's Task or file_XXX
        dir_name = dir_name.filename.parent

        
    matches = list(dir_name.rglob(pattern))
    if len(matches) == 1:
        return matches[0]
    elif len(matches) == 0:
        return find_nearest(dir_name.parent, pattern)
    else:
        matches_str = '"\n\t"'.join(str(x) for x in matches)
        raise FileNotFoundError(f'Multiple files matching "{pattern}":\n\t"{matches_str}"')

