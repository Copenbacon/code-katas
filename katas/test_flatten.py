"""Testing the flatten.py module."""
from random import choice, randint
from string import printable


def random_element():
    """Return a single random element Choices are an ASCII string character, boolean or a random integer."""
    return choice((
        choice(printable), choice((True, False)), randint(0, 1000)
    ))


def random_sequence():
    """Return a list with a maximum of one level of nesting."""
    return [choice((random_element(), [random_element() for _ in range(randint(1, 9))])) for _ in range(randint(5, 30))]


def solution(lst):
    """Other kind of solution."""
    result = []
    for a in lst:
        try:
            result.extend(a)
        except TypeError:
            result.append(a)
    return result


def test_flatten_me():
    """Test the flatten_me function."""
    from flatten import flatten_me
    assert flatten_me([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert flatten_me([['a', 'b'], 'c', ['d']]) == ['a', 'b', 'c', 'd']
    assert flatten_me(['!', '?']) == ['!', '?']
    assert flatten_me([[True, False], ['!'], ['?'], [71, '@']]) == [True, False, '!', '?', 71, '@']
    for _ in range(100):
        random_seq = random_sequence()
        assert solution(random_seq) == flatten_me(random_seq)
