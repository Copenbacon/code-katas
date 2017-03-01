"""Test the proper_parenthetics module."""
import pytest


OPEN_TABLE = [
    ["(", 1],
    ["((", 1],
    ["()(", 1],
    ["()", 0],
    ["(())", 0],
    [")(", -1],
    ["(()))(", -1],
]


@pytest.mark.parametrize("test_val, result", OPEN_TABLE)
def test_parenthetics_set(test_val, result):
    """Test that a set returns the correct value."""
    from proper_parenthetics import parenthetics
    assert parenthetics(test_val) == result
