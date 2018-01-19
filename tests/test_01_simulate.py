from nibabel import load as nload
from nibabel import Nifti1Image

from bidso.simulate.fmri import create_bold, create_events
from bidso.simulate import simulate_bold, simulate_ieeg, simulate_electrodes
from bidso.utils import bids_mkdir
from bidso import Task

from .paths import BIDS_PATH, T1_PATH, task_ieeg, task_fmri, task_anat, elec_ct


def test_simulate_root():

    participants_tsv = BIDS_PATH / 'participants.tsv'
    with participants_tsv.open('w') as f:
        f.write('participant_id\tage\tsex\n')

        f.write(f'{task_ieeg.subject}\t30\tF\n')


def test_simulate_ieeg():
    elec = simulate_electrodes(BIDS_PATH, elec_ct)
    simulate_ieeg(BIDS_PATH, task_ieeg, elec)


def test_simulate_anat():
    mri = nload(str(T1_PATH))
    x = mri.get_data()
    nifti = Nifti1Image(x, mri.affine)

    anat_path = bids_mkdir(BIDS_PATH, task_anat)
    nifti.to_filename(str(anat_path / f'sub-{task_anat.subject}_T1w.nii.gz'))


def test_simulate_fmri():
    simulate_bold(task_fmri, BIDS_PATH, T1_PATH)


def test_read_fmri():
    Task(task_fmri.get_filename(BIDS_PATH))
