"""Test convert_array.py."""
from convert_array import digitize


def test_digitize():
    """Testing the digitize function."""
    assert digitize(35231) == [1, 3, 2, 5, 3]
    assert digitize(23582357) == [7, 5, 3, 2, 8, 5, 3, 2]
    assert digitize(984764738) == [8, 3, 7, 4, 6, 7, 4, 8, 9]
    assert digitize(45762893920) == [0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4]
    assert digitize(548702838394) == [4, 9, 3, 8, 3, 8, 2, 0, 7, 8, 4, 5]


def test_random():
    """Test with random_ints."""
    from random import randint
    # Test.describe('Random tests')
    for x in range(37):
        y = randint(10, 99 * 2 ** x)
        print(digitize(y) == map(int, list(str(y)[::-1])))
        assert digitize(y) == list(map(int, list(str(y)[::-1])))
