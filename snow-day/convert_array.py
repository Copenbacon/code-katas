"""Convert a number (n) in a reverse list of the individual numbers."""


def digitize(n):
    """Convert a number into a reverse list of each individual number."""
    str_list = list(str(n))
    str_list.reverse()
    num_list = []
    for idx in range(len(str_list)):
        num_list.append(int(str_list[idx]))
    return num_list
