"""Test mult_delimiters.py."""
from mult_delimiters import multiple_split


def test_multiple_split():
    """Test the multiple_split method()."""
    assert multiple_split('Hi everybody!', [' ', '!']) == ['Hi', 'everybody']
    assert multiple_split('(1+2)*6-3^9', ['+', '-', '(', ')', '^', '*']) == ['1', '2', '6', '3', '9']
    assert multiple_split('Solve_this|kata-very\quickly!', ['!', '|', '\\', '_', '-']) == ['Solve', 'this', 'kata', 'very', 'quickly']
    assert multiple_split('', []) == []
    assert multiple_split('') == []
    assert multiple_split('some strange string') == ['some strange string']
    assert multiple_split('1_2_3_huhuh_hahaha', ['_']) == ['1', '2', '3', 'huhuh', 'hahaha']
    assert multiple_split('((1+2))*(6-3)^9', ['+', '-', '(', ')', '^', '*']) == ['1', '2', '6', '3', '9']
    assert multiple_split('(((1+2)-(3)))', ['(', ')']) == ['1+2', '-', '3']
