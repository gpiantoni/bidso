from bidso import iEEG
from bidso.find import find_nearest

from .paths import BIDS_PATH


def test_find_nearest():
    t = iEEG(BIDS_PATH / 'sub-bert/ses-day02/ieeg/sub-bert_ses-day02_task-block_run-00_ieeg.bin')
    assert find_nearest(t, 'anat').name == 'anat'
