from .files import file_Core, file_Json, file_Tsv
from .utils import replace_extension, replace_underscore, remove_underscore
from .find import find_in_bids


class Electrodes(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.electrodes = file_Tsv(filename)
        self.coordframe = file_Json(replace_underscore(self.filename, 'coordsystem.json'))

    def get_xyz(self, list_of_names=None):
        """Get xyz coordinates for these electrodes

        Parameters
        ----------
        list_of_names : list of str
            list of electrode names to use

        Returns
        -------
        list of tuples of 3 floats (x, y, z)
            list of xyz coordinates for all the electrodes

        TODO
        ----
        coordinate system of electrodes
        """
        if list_of_names is not None:
            filter_lambda = lambda x: x['name'] in list_of_names
        else:
            filter_lambda = None

        return self.electrodes.get(filter_lambda=filter_lambda,
                                   map_lambda=lambda e: (_float(e['x']),
                                                         _float(e['y']),
                                                         _float(e['z'])))

def _float(val):
    if val == 'n/a':
        return None
    else:
        return float(val)

class Task(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.json = file_Json(replace_extension(self.filename, '.json'))
        events = replace_underscore(self.filename, 'events.tsv')
        if not events.exists():  # remove only acq (workaround)
            s = events.name
            s = '_'.join(x for x in s.split('_') if not x.startswith('acq-'))
            events = events.parent / s
        if not events.exists():
            raise ValueError(f'could not find events as {events}')
        self.events = file_Tsv(events)


class iEEG(Task):
    electrodes = None
    channels = None

    def __init__(self, filename):
        super().__init__(filename)
        self.channels = file_Tsv(replace_underscore(self.filename, 'channels.tsv'))

    def read_electrodes(self, electrodes='*'):
        self.electrodes = Electrodes(find_in_bids(self.filename, upwards=True, acquisition=electrodes, modality='electrodes', extension='.tsv'))
