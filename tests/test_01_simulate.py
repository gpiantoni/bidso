from json import dump
from nibabel import load as nload
from nibabel import Nifti1Image

from bidso.simulate.fmri import create_bold, create_events
from bidso.utils import add_underscore
from bidso import Task

from .paths import BIDS_PATH, FREESURFER_PATH

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

T1_path = FREESURFER_PATH / 'bert/mri/T1.mgz'


def test_simulate_root():

    participants_tsv = BIDS_PATH / 'participants.tsv'
    with participants_tsv.open('w') as f:
        f.write('participant_id\tage\tsex\n')

        f.write(f'{subject}\t30\tF\n')


def test_simulate_anat():

    mri = nload(str(T1_path))
    x = mri.get_data()
    nifti = Nifti1Image(x, mri.affine)

    anat_path = BIDS_PATH / f'sub-{subject}/ses-{session}/anat/'
    anat_path.mkdir(parents=True)
    nifti.to_filename(str(anat_path / f'sub-{subject}_T1w.nii.gz'))


def test_simulate_fmri():
    mri = nload(str(T1_path))

    create_bold(mri, add_underscore(fmri_file, 'bold.nii.gz'))
    create_events(add_underscore(fmri_file, 'events.tsv'))

    with add_underscore(fmri_file, 'bold.nii.gz').open('w') as f:
        dump({}, f)


def test_read_fmri():

    Task(add_underscore(fmri_file, 'bold.nii.gz'))
