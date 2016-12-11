"""Test the Sum Series module."""
from sum_series import series_sum

# Basic tests
assert series_sum(1) == "1.00"
assert series_sum(2) == "1.25"
assert series_sum(3) == "1.39"
assert series_sum(4) == "1.49"
assert series_sum(5) == "1.57"
assert series_sum(6) == "1.63"
assert series_sum(7) == "1.68"
assert series_sum(8) == "1.73"
assert series_sum(9) == "1.77"
assert series_sum(15) == "1.94"
assert series_sum(39) == "2.26"
assert series_sum(58) == "2.40"
assert series_sum(0) == "0.00"


# Random tests
def test_randos():
    """It should work for random inputs too."""
    from random import randint
    sol = lambda n: '0.00' if n == 0 else (lambda s: s[:-2] + "." + s[-2:])(str(int(round(sum([1.0 / (1 + i * 3) for i in range(n)]) * 100))))
    for _ in range(40):
        n = randint(0, 100)
        print("Testing for " + str(n))
        assert series_sum(n) == sol(n)
