from bidso import (bids_Core,
                   bids_Tsv,
                   bids_Json,
                   bids_Channels,
                   bids_Events,
                   bids_Electrodes,
                   bids_Modality,
                   dir_Root,
                   )

from .paths import PATH_IEEG


def test_bids_File():
    bids_Modality(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_task-visual_run-01_ieeg.json')

    bids_Channels(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_task-visual_run-01_channels.tsv')

    bids_Events(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_task-visual_run-01_events.tsv')

    bids_Electrodes(PATH_IEEG / 'sub-01/ses-01/ieeg/sub-01_ses-01_acq-corrected_electrodes.tsv')

    bids_Json(PATH_IEEG / 'sub-01/ses-01/anat/sub-01_ses-01_T1w.json')


def test_bids_Dir():
    dir_Root(PATH_IEEG)
