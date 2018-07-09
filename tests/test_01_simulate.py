from sanajeh import simulate_all

from .paths import BIDS_PATH


def test_read_fmri():
    simulate_all(BIDS_PATH)
