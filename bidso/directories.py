from re import search
from json import load as json_load

from pathlib import Path

from .files import file_Tsv


class dir_Core():
    def __init__(self, dirname):
        self.dirname = Path(dirname)


class dir_Root(dir_Core):
    def __init__(self, dirname):
        super().__init__(dirname)

        self.participants = file_Tsv(self.dirname / 'participants.tsv')
        self.subjects = []
        for participant in self.participants.tsv:
            self.subjects.append(dir_Core(self.dirname / participant['participant_id']))
