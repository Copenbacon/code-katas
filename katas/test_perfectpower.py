from random import random, randrange
from math import log, floor
import pytest
from perfectpower import isPP
import sys

BASE_TABLE = [
    (4, [2, 2]),
    (9, [3, 2]),
    (5, None),
]


@pytest.mark.parametrize("input, result", BASE_TABLE)
def test_basics(input, result):
    """Perfect powers, should work for some examples."""
    assert(isPP(input) == result)


def test_first_pps():
    """Should work for the first perfect powers."""
    pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
    for item in pp:
        assert(isPP(item) is not None)


def test_randoms():
    """Should work for random perfect powers."""
    if int(sys.version[0]) > 2:
        for i in range(100):
            m = 2 + floor(random() * 255)
            k = 2 + floor(random() * log(268435455) / log(m))
            l = m**k
            r = isPP(l)
            if r is None:
                assert(m**k != l)
                break
            else:
                assert(type(r) == list)
    else:
        pass