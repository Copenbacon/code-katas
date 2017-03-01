"""Test module for prime.py."""
import pytest

PRIME_TABLE = [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (41, True),
    (45, False),
    (73, True),
    (75, False),
    (5099, True),
    (-1, False),
]


@pytest.mark.parametrize('input, result', PRIME_TABLE)
def test_prime_nums(input, result):
    from prime import is_prime
    assert(is_prime(input) == result)