from bidso.utils import replace_extension, replace_underscore, find_extension
from .paths import BIDS_PATH, elec_ct


def test_find_extension():
    assert find_extension(elec_ct.get_filename(BIDS_PATH)) == '.tsv'


def test_replace_extension():
    assert replace_extension('file.txt', '.bin') == 'file.bin'


def test_replace_underscore():
    assert replace_underscore('file_mod.txt', 'dat.txt') == 'file_dat.txt'
