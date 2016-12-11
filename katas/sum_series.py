"""Sum Series module from Codewars."""


def series_sum(n):
    """Sum a series of fractions up to the nth value."""
    answer = 0
    for series_len in range(1, 1 + n * 3, 3):
        answer += 1 / series_len
    return "{:.2f}".format(answer)
