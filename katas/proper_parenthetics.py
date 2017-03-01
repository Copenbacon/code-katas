"""
The Proper Parenthetics module.

Returns 1 for an open set of parentheses,
0 for a balanced set, and -1 for a
broken set.
"""
from dll import DLL


def parenthetics(string):
    """The parenthetics module checks for open, broken, or balanced sets."""
    matches = DLL()
    for char in string:
        if char == "(":
            matches.append(char)
        if char == ")":
            if matches.head is None or matches.pop() != "(":
                return -1
    if matches.head is None:
        return 0
    else:
        return 1
