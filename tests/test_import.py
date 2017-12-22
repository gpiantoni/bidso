from bidso import (file_Core,
                   file_Tsv,
                   file_Json,
                   file_Channels,
                   file_Events,
                   file_Electrodes,
                   file_Modality,
                   dir_Root,
                   )

from .paths import PATH_IEEG


def test_file_xxx():
    file_Modality(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_task-visual_run-01_ieeg.json')

    file_Channels(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_task-visual_run-01_channels.tsv')

    file_Events(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_task-visual_run-01_events.tsv')

    file_Electrodes(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_acq-corrected_electrodes.tsv')

    file_Json(PATH_IEEG / 'sub-01/ses-01/anat/sub-01_ses-01_T1w.json')


def test_directories_xxx():
    dir_Root(PATH_IEEG)
