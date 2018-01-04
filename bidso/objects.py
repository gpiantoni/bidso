from .files import file_Electrodes, file_Core, file_Json, file_Events
from .utils import replace_extension, replace_underscore, add_underscore


class Electrodes(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.electrodes = file_Electrodes(add_underscore(filename, 'electrodes.tsv'))
        self.coordframe = file_Json(add_underscore(self.filename, 'coordframe.json'))


class Task(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.events = file_Events(replace_underscore(self.filename, 'events.tsv'))
        self.json = file_Json(replace_extension(self.filename, '.json'))
