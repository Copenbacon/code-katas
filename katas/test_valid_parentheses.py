from valid_parentheses import valid_parentheses
import pytest

TEST_PARENTHESES = [
    (")", False),
    ("(", False),
    ("", True),
    ("hi)(", False),
    ("hi(hi)", True),
    ("(", False),
    ("hi(hi)(", False),
    ("((())()())", True),
    ("(c(b(a)))(d)", True),
    ("hi(hi))(", False),
]


@pytest.mark.parametrize('inputs, result', TEST_PARENTHESES)
def test_parentheses(inputs, result):
    assert valid_parentheses(inputs) == result


def test_randoms():
    base = "abcdefghijklmnopqrstuvwxyz()"
    from random import randint
    isSol = lambda string: all([string[:i].count(")")<=string[:i].count("(") for i in range(len(string)+1)]) and string.count("(") == string.count(")")
    for _ in range(40):
        testlen = randint(5, 40)
        teststring = ["()", "()()", "(())", "()(())()"][randint(0, 3)]
        for i in range(testlen):
            pos = randint(0, len(teststring))
            teststring = teststring[:pos] + base[randint(0, len(base) - 1)] + teststring[pos:]
        assert valid_parentheses(teststring) == isSol(teststring)