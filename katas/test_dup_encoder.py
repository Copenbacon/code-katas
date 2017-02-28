"""Test Module for Duplicate Encoder Kata from CodeWars."""
import pytest
from random import randint
from dup_encoder import duplicate_encode

DUP_TABLE = [
    ("din", "((("),
    ("recede", "()()()"),
    ("Success", ")())())"),
    ("CodeWarrior", "()(((())())"),
    ("Supralapsarian", ")()))()))))()("),
    ("iiiiii", "))))))"),
    ("(( @", "))(("),
    (" ( ( )", ")))))(")
]


"""Basic tests."""


@pytest.mark.parametrize('input, result', DUP_TABLE)
def test_basics(input, result):
    """Testing Basic Inputs."""
    assert(duplicate_encode(input) == result)


"""And now... some random tests !"""


def test_randoms():
    """Testing Random Inputs"""
    duplicate_sol = lambda word: "".join(["(" if word.lower().count(x.lower()) == 1 else ")" for x in word])
    for _ in range(40):
        testlen = randint(6, 40)
        testword = ""
        for i in range(testlen):
            testword += "abcdeFGHIJklmnOPQRSTuvwxyz() @!"[randint(0, 30)]
        assert(duplicate_encode(testword) == duplicate_sol(testword))
