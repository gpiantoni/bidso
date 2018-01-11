from json import dump
from nibabel import load as nload

from bidso.simulate.fmri import create_bold, create_events
from bidso.utils import add_underscore
from bidso import Task

from .paths import BIDS_PATH

subject = 'bert'
session = 'day01'
modality = 'func'

subj_path = BIDS_PATH / f'sub-{subject}'
subj_path.mkdir()

sess_path = subj_path / f'ses-{session}'
sess_path.mkdir()

modality_path = sess_path / f'{modality}'
modality_path.mkdir()
fmri_file = modality_path / f'sub-{subject}_ses-{session}_task-block_run-00'


def test_simulate_fmri():
    mri = nload('tests/data/derivatives/freesurfer/bert/mri/T1.mgz')  # TODO

    create_bold(mri, add_underscore(fmri_file, 'bold.nii.gz'))
    create_events(add_underscore(fmri_file, 'events.tsv'))

    with add_underscore(fmri_file, 'bold.nii.gz').open('w') as f:
        dump({}, f)


def test_read_fmri():

    Task(add_underscore(fmri_file, 'bold.nii.gz'))
