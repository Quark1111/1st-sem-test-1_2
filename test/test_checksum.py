from src.checksum import modulo11Checksum


def test_bad():
    assert not modulo11Checksum("2-266-11156-3")


def test_good_without_hyphens():
    assert modulo11Checksum("2266111568")


def test_good_with_x_check_digit():
    assert modulo11Checksum("0-304-33376-")


def test_bad_wrong_length_long():
    assert modulo11Checksum("1234567890123") == -1


def test_bad_wrong_length_short():
    assert modulo11Checksum("12345") == -1
