from nibabel import load as nload

from .paths import BIDS_PATH


def test_simulate_fmri():
    mri = nload('tests/data/derivatives/freesurfer/bert/mri/T1.mgz')  # TODO

    fmri_file = modality_path / f'sub-{info["subject"]}_ses-{info["session"]}_task-block_run-00'

    _create_bold(mri, add_underscore(fmri_file, 'bold.nii.gz'))
    _create_events(add_underscore(fmri_file, 'events.tsv'))
