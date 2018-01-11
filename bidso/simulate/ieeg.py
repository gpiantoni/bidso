from shutil import copyfile
from json import dump
from pathlib import Path


from ..utils import replace_underscore


DATA_PATH = Path(__file__).resolve().parent / 'data'


def create_electrodes(output_file):
    electrodes_file = DATA_PATH / 'electrodes.tsv'
    copyfile(electrodes_file, output_file)

    coordframe_file = replace_underscore(output_file, 'coordframe.json')
    with coordframe_file.open('w') as f:
        dump({}, f)
