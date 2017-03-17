"""Refactored testing module from Codewars"""
import pytest
from valid_braces import validBraces

VALID_TABLE = [
    ("()"),
    ("[]"),
    ("{}"),
    ("{}()[]"),
    ("([{}])"),
    ("{}({})[]"),
    ("(({{[[]]}}))"),
]

INVALID_TABLE = [
    ("(}"),
    ("([}{])"),
    ("(((({{"),
    (")(}{]["),
    ("())({}}{()][]["),
]


@pytest.mark.parametrize("string", VALID_TABLE)
def test_valid(string):
    assert validBraces(string) is True


@pytest.mark.parametrize("string", INVALID_TABLE)
def test_invalid(string):
    assert validBraces(string) is False
