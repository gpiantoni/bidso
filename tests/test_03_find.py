from bidso import iEEG
from bidso.find import find_modality

from .paths import BIDS_PATH


def test_find_modality():
    t = iEEG(BIDS_PATH / 'sub-bert/ses-day02/ieeg/sub-bert_ses-day02_task-block_run-00_ieeg.bin')
    assert find_modality(t, 'anat').name == 'anat'
