from extend_noip import __version__


def test_version():
    assert __version__[:3] == "0.1"
