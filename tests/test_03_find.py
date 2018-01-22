from pytest import raises, warns
from bidso.find import find_in_bids, find_root, _generate_pattern

from .paths import BIDS_PATH, task_ieeg

filename = task_ieeg.get_filename(BIDS_PATH)


def test_find_root():
    assert find_root(filename).name == 'bids'
    assert find_root(filename, target='subject').name == 'sub-bert'
    assert find_root(filename, target='session').name == 'ses-day02'


def test_find_nearest_01():

    found = find_in_bids(filename, subject='bert', session='day01', run='00',
                         extension='.nii.gz', upwards=True)
    assert found.name == 'sub-bert_ses-day01_task-block_run-00_bold.nii.gz'

    with warns(UserWarning):
        find_in_bids(filename, subject='bert', useless='xxx', task='block',
                     modality='channels', upwards=True)


def test_find_nearest_02():

    with raises(FileNotFoundError):
        find_in_bids(filename, subject='xxx')


def test_find_nearest_03():

    with raises(FileNotFoundError):
        find_in_bids(filename, subject='bert')

def test_generate_pattern():
    assert _generate_pattern(dict(subject='test')) == 'sub-test_*.*'
    assert _generate_pattern(dict(subject='test', session='sess')) == 'sub-test_ses-sess_*.*'
    assert _generate_pattern(dict(subject='test', modality='mod')) == 'sub-test_*_mod.*'
    assert _generate_pattern(dict(session='sess', extension='.nii.gz')) == '*_ses-sess_*.nii.gz'
    assert _generate_pattern(dict(modality='mod', extension='.nii.gz')) == '*_mod.nii.gz'
