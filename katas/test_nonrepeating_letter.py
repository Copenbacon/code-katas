"""Test Module for nonrepeating letter.py"""
import pytest
from nonrepeating_letter import first_non_repeating_letter
from random import randint

TEST_STRINGS = [
    ('a', 'a'),
    ('stress', 't'),
    ('moonmen', 'e'),
    ('', ''),
    ('abba', ''),
    ('aa', ''),
    ('~><#~><', '#'),
    ('hello world, eh?', 'w'),
    ('sTreSS', 'T'),
    ('Go hang a salami, I\'m a lasagna hog!', ',')
]


"""Basic Tests"""


@pytest.mark.parametrize("input, result", TEST_STRINGS)
def test_non_repeat(input, result):
    assert(first_non_repeating_letter(input) == result)

"""Random Tests"""
def test_randoms():
    sol=lambda s: (lambda uniq: ([a for a in s if s.lower().count(a.lower()) == 1] or [""])[0])(set(s.lower()))
    base = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789;,:."

    for _ in range(40):
        s = "".join([base[randint(0, len(base) - 1)] for q in range(randint(10, 60))])
        assert(first_non_repeating_letter(s) == sol(s))