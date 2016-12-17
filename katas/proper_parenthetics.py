"""
The Proper Parenthetics module.

Returns 1 for an open set of parentheses,
0 for a balanced set, and -1 for a
broken set.
"""


def parenthetics(string):
    """The parenthetics module checks for open, broken, or balanced sets."""
    matches = []
    for char in string:
        if char == "(":
            matches.append(char)
        if char == ")":
            if matches == [] or matches.pop() != "(":
                return -1
    if matches == []:
        return 0
    else:
        return 1
