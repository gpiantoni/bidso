from re import search
from json import load as json_load

from pathlib import Path


class file_Core():
    def __init__(self, filename):
        self.filename = Path(filename)
        self.subject = _match(self.filename, 'sub-([a-zA-Z0-9\-]+)_')
        self.session = _match(self.filename, '_ses-([a-zA-Z0-9\-]+)_')
        self.run = _match(self.filename, '_run-([a-zA-Z0-9\-]+)_')
        self.acq = _match(self.filename, '_acq-([a-zA-Z0-9\-]+)_')


class file_Tsv(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.tsv = _read_tsv(self.filename)


class file_Json(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        with self.filename.open() as f:
            self.json = json_load(f)


class file_Channels(file_Tsv):
    def __init__(self, filename):
        super().__init__(filename)


class file_Events(file_Tsv):
    def __init__(self, filename):
        super().__init__(filename)


class file_Electrodes(file_Tsv):
    def __init__(self, filename):
        super().__init__(filename)


class file_Modality(file_Json):
    def __init__(self, filename):
        super().__init__(filename)


def _read_tsv(filename):
    with filename.open() as f:
        hdr = f.readline()
        tsv = []
        for l in f:
            d = {k.strip(): v.strip() for k, v in zip(hdr.split('\t'), l.split('\t'))}
            tsv.append(d)
    return tsv


def _match(filename, pattern):
    m = search(pattern, filename.stem)
    if m is None:
        return m
    else:
        return m.group(1)
