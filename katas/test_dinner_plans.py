"""Test dinner_plans.py module."""
from dinner_plans import common_ground


def test_common_ground():
    """Test the common_ground function."""
    # Basic tests
    assert common_ground("eat chicken", "eat chicken and rice") == 'eat chicken'
    assert common_ground("eat a burger and drink a coke", "drink a coke") == 'drink a coke'
    assert common_ground("i like turtles", "what are you talking about") == 'death'
    assert common_ground("aa bb", "aa bb cc") == "aa bb"
    assert common_ground("aa bb cc", "bb cc") == 'bb cc'
    assert common_ground("aa bb cc", "bb cc bb aa") == 'bb cc aa'
    assert common_ground("aa bb", "cc dd") == 'death'
    assert common_ground("aa bb", "") == 'death'
    assert common_ground("", "cc dd") == 'death'
    assert common_ground("", "") == 'death'


def test_random():
    """Test with random inputs."""
    # Random tests
    from random import randint
    sol = lambda s1, s2: (lambda s1, s2: " ".join([s for i, s in enumerate(s2) if s in s1 and s2.index(s) == i]))(s1.split(" "), s2.split(" ")) or "death"
    base = ["the", "in", "for", "on", "to", "from", "the", "in", "for", "on", "to", "from", "battle", "Pippi", "war", "peace", "treaty", "food", "drink", "alliance", "friend", "enemy", "attack", "defend", "observe", "consult", "ask", "advice", "soldier", "general", "spear", "sword", "shield", "bow", "quiver", "armour", "arrow", "meet", "assault", "catapult"]
    for _ in range(40):
        s1, s2 = [" ".join([base[randint(0, len(base) - 1)] for q in range(randint(1, 35))]) for k in range(2)]
        print("Testing for %s and %s" % (repr(s1), repr(s2)))
        assert common_ground(s1, s2) == sol(s1, s2)
