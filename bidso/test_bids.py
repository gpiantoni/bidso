from re import search
from nibabel import load as ni_load
from json import load as json_load

from pathlib import Path


class bids_Core():
    def __init__(self, filename):
        self.filename = Path(filename)
        self.subject = _match(self.filename, 'sub-([a-zA-Z0-9]+)_')
        self.session = _match(self.filename, '_ses-([a-zA-Z0-9]+)_')
        self.run = _match(self.filename, '_run-([a-zA-Z0-9]+)_')

class bids_Tsv(bids_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.tsv = _read_tsv(self.filename)

class bids_Json(bids_Core):
    def __init__(self, filename):
        super().__init__(filename)
        with self.filename.open() as f:
            self.json = json_load(f)

class bids_Channels(bids_Tsv):
    def __init__(self, filename):
        super().__init__(filename)


class bids_Events(bids_Tsv):
    def __init__(self, filename):
        super().__init__(filename)


class bids_Electrodes(bids_Tsv):
    def __init__(self, filename):
        super().__init__(filename)


class bids_Modality(bids_Json):
    def __init__(self, filename):
        super().__init__(filename)


class dir_Core():
    def __init__(self, dirname):
        self.dirname = Path(dirname)

class dir_Root(dir_Core):
    def __init__(self, dirname):
        super().__init__(dirname)

        self.participants = bids_Tsv(self.dirname / 'participants.tsv')
        self.subjects = []
        for participant in self.participants.tsv:
            self.subjects.append(dir_Core(self.dirname / participant['participant_id']))


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
