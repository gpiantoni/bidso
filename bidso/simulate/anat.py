from nibabel import load as nload
from nibabel import Nifti1Image

from ..files import file_Core
from ..utils import bids_mkdir


def simulate_anat(root, task_anat, t1):
    mri = nload(str(t1))
    x = mri.get_data()
    nifti = Nifti1Image(x, mri.affine)

    anat_path = bids_mkdir(root, task_anat)
    nifti.to_filename(str(anat_path / f'sub-{task_anat.subject}_T1w.nii.gz'))

    return file_Core(anat_path)  # use the general file_Core (Task needs events.tsv)
