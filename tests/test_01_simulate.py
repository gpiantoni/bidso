from nibabel import load as nload
from nibabel import Nifti1Image

from bidso.simulate.fmri import create_bold, create_events
from bidso.simulate.ieeg import (create_electrodes,
                                 create_channels,
                                 create_ieeg_info,
                                 create_ieeg_data,
                                 )
from bidso.utils import add_underscore, replace_underscore, replace_extension, bids_mkdir
from bidso import Task, Electrodes

from .paths import BIDS_PATH, T1_PATH, task_ieeg, task_fmri, task_anat, elec_ct


def test_simulate_root():

    participants_tsv = BIDS_PATH / 'participants.tsv'
    with participants_tsv.open('w') as f:
        f.write('participant_id\tage\tsex\n')

        f.write(f'{task_ieeg.subject}\t30\tF\n')


def test_simulate_ieeg():
    modality_path = bids_mkdir(BIDS_PATH, task_ieeg)

    elec_file = elec_ct.get_filename(BIDS_PATH)
    create_electrodes(elec_file)

    ieeg_file = modality_path / task_ieeg.get_filename()
    create_events(replace_underscore(ieeg_file, 'events.tsv'))

    elec = Electrodes(elec_file)
    n_elec = len(elec.electrodes.tsv)
    create_ieeg_data(ieeg_file, n_elec)

    create_ieeg_info(replace_extension(ieeg_file, '.json'))
    create_channels(replace_underscore(ieeg_file, 'channels.tsv'), elec)


def test_simulate_anat():
    mri = nload(str(T1_PATH))
    x = mri.get_data()
    nifti = Nifti1Image(x, mri.affine)

    anat_path = bids_mkdir(BIDS_PATH, task_anat)
    nifti.to_filename(str(anat_path / f'sub-{task_anat.subject}_T1w.nii.gz'))


def test_simulate_fmri():
    bids_mkdir(BIDS_PATH, task_fmri)
    mri = nload(str(T1_PATH))

    fmri_file = task_fmri.get_filename(BIDS_PATH)
    create_bold(mri, fmri_file)
    create_events(replace_underscore(fmri_file, 'events.tsv'))


def test_read_fmri():
    modality_path = bids_mkdir(BIDS_PATH, task_fmri)
    fmri_file = modality_path / f'sub-{task_fmri.subject}_ses-{task_fmri.session}_task-block_run-00'

    Task(add_underscore(fmri_file, 'bold.nii.gz'))
