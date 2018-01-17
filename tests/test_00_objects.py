from pytest import raises
from bidso import file_Core


def test_create_file_Core():
    core = file_Core(subject='a', session='b')
    assert core.subject == 'a'
    assert core.run is None
    
    with raises(KeyError):
        core = file_Core(weird='a')