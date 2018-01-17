from pathlib import Path
from functools import namedtuple


TEST_PATH = Path(__file__).resolve().parent
DATA_PATH = TEST_PATH / 'data'
BIDS_PATH = DATA_PATH / 'bids'
BIDS_PATH.mkdir(parents=True, exist_ok=True)
DERIVATIVES_PATH = DATA_PATH / 'derivatives'
FREESURFER_PATH = DERIVATIVES_PATH / 'freesurfer'


# this has a similar signature to Task, but Task is tested later
TaskSimple = namedtuple('BIDS', ('subject', 'session', 'modality', 'task', 'run'))

subject = 'bert'
task_fmri = TaskSimple(subject, 'day01', 'func', 'block', '00')
task_anat = TaskSimple(subject, 'day01', 'anat', 'block', '00')
task_ieeg = TaskSimple(subject, 'day02', 'ieeg', 'block', '00')

T1_PATH = FREESURFER_PATH / 'bert/mri/T1.mgz'
