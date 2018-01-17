from bidso import iEEG
from bidso.find import find_nearest

from .paths import BIDS_PATH


def test_find_nearest_01():

    found = find_nearest(filename, subject='bert', session='day01', extension='.nii.gz')
    assert found.stem == 'sub-bert_ses-day01_task-block_run-00_bold'
    
    
def test_find_nearest_02():
    
    with raises(FileNotFoundError):
        find_nearest(filename, subject='xxx')
    
    
def test_find_nearest_03():
    
    with raises(FileNotFoundError):
        find_nearest(filename, subject='bert')