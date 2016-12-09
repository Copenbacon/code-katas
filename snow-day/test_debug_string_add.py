"""Test the add function from the debug string module."""
from debug_string_add import add_stuff


def randsfg():
    """To make sure the user doesn't use a similar variable name."""
    import random
    s = ''
    for x in range(1, random.randint(0, 20)):
        s += chr(random.randint(96, 96 + 26))
    return s


def tadd(s1, s2):
    """Some code from the CodeWars Test Cases."""
    s1 = s1.encode()
    s2 = s2.encode()
    s1 = sum(s1)
    s2 = sum(s2)
    return s1 + s2


def test_debug_add():
    """Test the add_stuff func."""
    assert add_stuff('a', 'b') == 195
    for t in range(0, 100):
        s1 = randsfg()
        s2 = randsfg()
        assert add_stuff(s1, s2) == tadd(s1, s2)
