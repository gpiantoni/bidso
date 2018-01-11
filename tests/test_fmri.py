from nibabel import load as nload

from bidso.simulate.fmri import create_bold, create_events
from bidso.utils import add_underscore

from .paths import BIDS_PATH


def test_simulate_fmri():
    mri = nload('tests/data/derivatives/freesurfer/bert/mri/T1.mgz')  # TODO

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

    create_bold(mri, add_underscore(fmri_file, 'bold.nii.gz'))
    create_events(add_underscore(fmri_file, 'events.tsv'))
