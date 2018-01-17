from .files import file_Electrodes, file_Core, file_Json, file_Events, file_Channels
from .utils import replace_extension, replace_underscore
from .find import find_nearest


class Electrodes(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.electrodes = file_Electrodes(filename)
        self.coordframe = file_Json(replace_underscore(self.filename, 'coordframe.json'))


class Task(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.events = file_Events(replace_underscore(self.filename, 'events.tsv'))
        self.json = file_Json(replace_extension(self.filename, '.json'))


class iEEG(Task):
    def __init__(self, filename, electrodes='*'):
        super().__init__(filename)
        self.channels = file_Channels(find_nearest(self.filename, '*_channels.tsv'))
        self.electrodes = Electrodes(find_nearest(self.filename, electrodes + '_electrodes.tsv'))
