"""Flatten lists."""


def flatten_me(lst):
    """Flatten the list."""
    new_list = []
    for value in lst:
        if type(value) == list:
            new_list.extend(value)
        else:
            new_list.append(value)
    return new_list
