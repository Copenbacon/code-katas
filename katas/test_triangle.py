import pytest
from triangle import is_triangle

TRIANGLE_TABLE = [
	[1, 2, 2, True],
	[7, 2, 2, False],
	[1, 2, 3, False],
	[1, 3, 2, False],
	[3, 1, 2, False],
	[5, 1, 2, False],
	[1, 2, 5, False],
	[2, 5, 1, False],
	[4, 2, 3, True],
	[5, 1, 5, True],
	[2, 2, 2, True],
	[-1, 2, 3, False],
	[1, -2, 3, False],
	[1, 2, -3, False],
	[0, 2, 3, False]
]


"""Random sides."""
from random import randint

def solution(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

@pytest.mark.parametrize("val1, val2, val3, result", TRIANGLE_TABLE)
def test_is_triangle(val1, val2, val3, result):
	"""Test the smaller examples."""
	assert is_triangle(val1, val2, val3) == result

def test_randos():
	for _ in range(40):
	    a, b, c = [randint(-2, 10) for i in range(3)]
	    assert is_triangle(a, b, c) == solution(a, b, c)