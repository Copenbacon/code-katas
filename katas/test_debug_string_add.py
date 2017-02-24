"""Test the add function from the debug string module."""
import pytest

ADD_TABLE = [
    ["a", "b", 195],
    ["ab", "b", 293],
    ["abc", "c", 393],
    ["Lassie", "RinTinTin", 1504]
]

"""I don't understand these tests and they don't work in py2."""
# def randsfg():
#     """To make sure the user doesn't use a similar variable name."""
#     import random
#     s = ''
#     for x in range(1, random.randint(0, 20)):
#         s += chr(random.randint(96, 96 + 26))
#     return s


# def tadd(s1, s2):
#     """Some code from the CodeWars Test Cases."""
#     s1 = s1.encode()
#     s2 = s2.encode()
#     s1 = sum(s1)
#     s2 = sum(s2)
#     return s1 + s2

@pytest.mark.parametrize("val1, val2, result", ADD_TABLE)
def test_debug_add(val1, val2, result):
    """Test the add_stuff func."""
    from debug_string_add import add_stuff
    assert add_stuff(val1, val2) == result
