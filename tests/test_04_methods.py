from bidso.files import file_Tsv
from .paths import elec_ct, BIDS_PATH


def test_file_Tsv_get():

    tsv = file_Tsv(elec_ct.get_filename(BIDS_PATH))

    assert tsv.get(lambda x: x['name'] == 'grid01')[0]['name'] == 'grid01'
    assert tsv.get(None, lambda x: x['name'])[0] == 'grid01'
