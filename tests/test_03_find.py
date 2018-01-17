from pytest import raises, warns
from bidso.find import find_nearest, find_root

from .paths import BIDS_PATH

filename = BIDS_PATH / 'sub-bert/ses-day02/ieeg/sub-bert_ses-day02_task-block_run-00_ieeg.bin'


def test_find_root():
    assert find_root(filename).name == 'bids'
    assert find_root(filename, target='subject').name == 'sub-bert'
    assert find_root(filename, target='session').name == 'ses-day02'


def test_find_nearest_01():

    found = find_nearest(filename, subject='bert', session='day01', run='00',
                         extension='.nii.gz')
    assert found.name == 'sub-bert_ses-day01_task-block_run-00_bold.nii.gz'

    with warns(UserWarning):
        find_nearest(filename, subject='bert', useless='xxx', task='block',
                     modality='channels')


def test_find_nearest_02():

    with raises(FileNotFoundError):
        find_nearest(filename, subject='xxx')


def test_find_nearest_03():

    with raises(FileNotFoundError):
        find_nearest(filename, subject='bert')
