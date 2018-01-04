def replace_extension(filename, suffix):
    return filename.parent / (filename.name.split('.')[0] + suffix)


def replace_underscore(filename, suffix):
    return filename.parent / ('_'.join(filename.name.split('_')[:-1] + [suffix, ]))


def add_underscore(filename, suffix):
    return filename.parent / (filename.name + '_' + suffix)
