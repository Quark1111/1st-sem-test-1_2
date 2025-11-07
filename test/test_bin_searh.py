from src.bin_search import binSearch
def test_middle():
    assert binSearch([1, 2, 3, 4, 5], 4) == 3


def test_start():
    assert binSearch([1, 2, 3, 4], 2) == 1


def test_last_element():
    assert binSearch([1, 2, 3, 4, 5], 5) == 4


def test_single_element_found():
    assert binSearch([42], 42) == 0


def test_single_element_not_found():
    assert binSearch([42], 100) == -1


def test_empty_array():
    assert binSearch([], 5) == -1
