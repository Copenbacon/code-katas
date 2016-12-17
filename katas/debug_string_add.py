"""Add a string's characters together as encoded numbers."""


def add_stuff(s1, s2):
    """Add two strings together as numbers."""
    a1 = 0
    a2 = 0
    for char in range(len(s1)):
        a1 += ord(s1[char])
    for char in range(len(s2)):
        a2 += ord(s2[char])
    return a1 + a2
