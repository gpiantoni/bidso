from bidso import (Task,
                   )

from bidso.utils import find_root

from bidso.files import (file_Json,
                         file_Events,
                         file_Modality,
                         )

from bidso.directories import (dir_Root,
                               dir_Session,
                               )

from .paths import BIDS_PATH


def test_file_xxx():
    file_Modality(BIDS_PATH / 'sub-01/ses-01/ieeg/sub-01_ses-01_task-visual_run-01_ieeg.json')

    json_file = file_Json(BIDS_PATH / 'sub-bert/ses-day01/func/sub-bert_ses-day01_task-block_run-01_bold.json')
    find_root(json_file.filename)


def test_directories_xxx():
    dir_Root(BIDS_PATH)

    dir_Session(BIDS_PATH / 'sub-bert/ses-day01')


def test_objects_xxx():
    Task(BIDS_PATH / 'sub-bert/ses-day01/func/sub-bert_ses-day01_task-block_run-01_bold.nii.gz')
