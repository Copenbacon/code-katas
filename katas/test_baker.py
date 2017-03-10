"""Test suite for baker."""
from baker import cakes
import pytest
from random import shuffle, randrange


CAKE_TABLE = [
    ({"flour": 500, "sugar": 200, "eggs": 1},
     {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}, 2),
    ({"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
     {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream":
      5000}, 11),
    ({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
     {"sugar": 500, "flour": 2000, "milk": 2000}, 0),
    ({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
     {"sugar": 500, "flour": 2000, "milk": 2000, "apples": 15, "oil": 20}, 0),
    ({"eggs": 4, "flour": 400}, {}, 0),
    ({"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1},
     {"sugar": 1, "eggs": 1, "flour": 3, "cream": 1, "oil": 1, "milk": 1}, 1)
]


@pytest.mark.parametrize("recipe, available, result", CAKE_TABLE)
def test_cake(recipe, available, result):
    assert cakes(recipe, available) == result

ingredients = ['flour', 'eggs', 'oil', 'milk', 'apples', 'sugar', 'cream', 'pears', 'butter', 'nuts', 'chocolate', 'cocoa', 'crumbles'];
