"""Testing sea_sick.py module."""
from sea_sick import sea_sick


def test_sea_sick():
    """Basic tests."""
    sea_sick("~") == "No Problem"
    sea_sick("_~~~~~~~_~__~______~~__~~_~~") == "Throw Up"
    sea_sick("______~___~_") == "Throw Up"
    sea_sick("____") == "No Problem"
    sea_sick("_~~_~____~~~~~~~__~_~") == "Throw Up"


def test_rands():
    """Random tests."""
    from random import randint
    sol = lambda s: ["No Problem", "Throw Up"][(s.count("~_") + s.count("_~")) / float(len(s)) > 0.2]

    for _ in range(40):
        base = ["_____~", "~~~~~_"][randint(0, 1)]
        s = "".join([base[randint(0, len(base) - 1)] for q in range(randint(2, 25))])
        assert sea_sick(s) == sol(s)
