from json import load as json_load
from pathlib import Path

from .utils import read_tsv, _match, find_extension, add_modality, remove_extension


class file_Core():
    filename = None
    subject = None
    session = None
    modality = None
    run = None
    acquisition = None
    task = None
    extension = None

    def __init__(self, filename=None, **kwargs):
        if filename is not None:
            self.filename = Path(filename)
            self.subject = _match(self.filename, 'sub-([a-zA-Z0-9\-]+)_')
            self.session = _match(self.filename, '_ses-([a-zA-Z0-9\-]+)_')
            self.modality = remove_extension(self.filename.name).split('_')[-1]
            self.run = _match(self.filename, '_run-([a-zA-Z0-9\-]+)_')
            self.acquisition = _match(self.filename, '_acq-([a-zA-Z0-9\-]+)_')
            self.task = _match(self.filename, '_task-([a-zA-Z0-9\-]+)_')
            self.extension = find_extension(self.filename)

        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
                else:
                    raise KeyError(f'"{k}" is not an attribute of file_Core')

    def get_filename(self, base_dir=None):

        filename = 'sub-' + self.subject
        if self.session is not None:
            filename += '_ses-' + self.session
        if self.task is not None:
            filename += '_task-' + self.task
        if self.run is not None:
            filename += '_run-' + self.run
        if self.acquisition is not None:
            filename += '_acq-' + self.acquisition
        if self.modality is not None:
            filename += '_' + self.modality
        if self.extension is not None:
            filename += self.extension

        if base_dir is None:
            return filename

        else:
            dir_name = base_dir / ('sub-' + self.subject)
            if self.session is not None:
                dir_name /= 'ses-' + self.session
            dir_name = add_modality(dir_name, self.modality)

            return dir_name / filename


class file_Tsv(file_Core):
    def __init__(self, filename):
        super().__init__(filename)
        self.tsv = read_tsv(self.filename)


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
