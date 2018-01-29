from shutil import copyfile
from json import dump
from pathlib import Path
from numpy import ones, memmap, r_
from numpy import random


from ..objects import Electrodes, iEEG
from ..utils import replace_underscore, replace_extension, bids_mkdir
from .fmri import create_events


DATA_PATH = Path(__file__).resolve().parent / 'data'

sf = 256
dur = 192
AMPLITUDE = 1000
EFFECT_SIZE = 2
block_dur = 32
EXTRA_CHANS = ('EOG1', 'EOG2', 'ECG', 'EMG', 'other')


def simulate_ieeg(root, ieeg_task, elec):
    bids_mkdir(root, ieeg_task)

    n_elec = len(elec.electrodes.tsv)
    ieeg_file = ieeg_task.get_filename(root)

    create_ieeg_data(ieeg_file, n_elec)
    create_ieeg_info(replace_extension(ieeg_file, '.json'))
    create_channels(replace_underscore(ieeg_file, 'channels.tsv'), elec)
    create_events(replace_underscore(ieeg_file, 'events.tsv'))

    return iEEG(ieeg_file)


def simulate_electrodes(root, elec_obj, electrodes_file=None):
    bids_mkdir(root, elec_obj)

    if electrodes_file is None:
        electrodes_file = DATA_PATH / 'electrodes.tsv'
    output_file = elec_obj.get_filename(root)
    copyfile(electrodes_file, output_file)

    coordframe_file = replace_underscore(output_file, 'coordframe.json')
    COORDFRAME = {
        'iEEGCoordinateSystem': 'tkRAS',
        'iEEGCoordinateProcessingDescripton': '',
        }
    with coordframe_file.open('w') as f:
        dump(COORDFRAME, f, indent=' ')

    return Electrodes(output_file)


def create_ieeg_data(output_file, n_elec):

    n_chan = n_elec + len(EXTRA_CHANS)

    random.seed(100)
    t = r_[ones(block_dur * sf) * EFFECT_SIZE, ones(block_dur * sf), ones(block_dur * sf) * EFFECT_SIZE, ones(block_dur * sf), ones(block_dur * sf) * EFFECT_SIZE, ones(block_dur * sf)]
    data = random.random((n_chan, sf * dur)) * t[None, :] * AMPLITUDE

    dtype = 'float64'
    memshape = (n_chan, sf * dur)
    mem = memmap(str(output_file), dtype, mode='w+', shape=memshape, order='F')
    mem[:, :] = data
    mem.flush()


def create_channels(output_file, elec):
    with output_file.open('w') as f:
        f.write('name\ttype\tsampling_frequency\tunits\tstatus\n')
        for one_elec in elec.electrodes.tsv:
            f.write(f'{one_elec["name"]}\tECoG\t{sf}\tmicroV\tgood\n')

        for chan_name in EXTRA_CHANS:
            f.write(f'{chan_name}\tother\t{sf}\tmicroV\tgood\n')


def create_ieeg_info(output_file):
    dataset_info = {
        "TaskName": "block",
        "Manufacturer": "simulated",
        "TaskDescription": "block design",
        "Instructions": "nothing",
        "InstitutionName": "",
        "InstitutionAddress": "",
        "EEGChannelCount": 0,
        "EOGChannelCount": 0,
        "ECGChannelCount": 0,
        "EMGChannelCount": 0,
        "MiscChannelCount": 0,
        "TriggerChannelCount": 0,
        "PowerLineFrequency": 50,
        "RecordingDuration": dur,
        "RecordingType": "continuous",
        "EpochLength": 0,
        "iEEGSurfChannelCount": 0,
        "iEEGDepthChannelCount": 0,
        "iEEGPlacementScheme": "",
        "iEEGReferenceScheme": ""
    }

    with output_file.open('w') as f:
        dump(dataset_info, f, indent=' ')
