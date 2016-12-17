"""Dinner Plans Kata from Codewars."""


def common_ground(s1, s2):
    """Test that s1 and s2 have similar words."""
    from collections import OrderedDict
    result = []
    for val in s2.split():
        if val in s1.split():
            result.append(val)
    result = ' '.join(OrderedDict.fromkeys(result))
    if result == '':
        result = 'death'
    return result
