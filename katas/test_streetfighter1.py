import pytest
import random
from streetfighter1 import street_fighter_selection

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
opts = ["up", "down", "right", "left"]

"""Character selection."""


def test_no_selection():
    """Should work with no selection cursor moves."""
    moves = []
    solution = []
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


def test_left():
    """Should go left 8 times."""
    moves = ["left"] * 8
    solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


def test_right():
    """Should go right 8 times."""
    moves = ["right"] * 8
    solution = ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


def test_up():
    """Should go up 4 times, always the same."""
    moves = ["up"] * 4
    solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


def test_down():
    """Should go down 4 times, always the same."""
    moves = ["down"] * 4
    solution = ['Ken', 'Ken', 'Ken', 'Ken']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


def test_clockwise():
    """Should use all 4 directions counter-clockwise twice."""
    moves = ["down", "right", "up", "left"] * 2
    solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


def test_clockwise_twice():
    """Should use all 4 directions clockwise twice."""
    moves = ["up", "left", "down", "right"] * 2
    solution = ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


def test_all_chars():
    """Should cover all characters."""
    moves = ["up"] + ["left"] * 6 + ["down"] + ["right"] * 6
    solution = ['Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 
                'Ken', 'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Ken']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution


"""Random Tests now!"""


def my_street_fighter_selection(fighters, position, moves):
    dirs = {"up": -1, "down": 1, "left": -1, "right": 1}
    res = []
    for i in moves:
        if i == "up":
            position = (max(0, position[0] - 1), position[1])
        if i == "down":
            position = (min(1, position[0] + 1), position[1])
        if i in ["left", "right"]:
            position = (position[0], (position[1] + dirs[i]) % len(fighters[position[0]]))
        # print i, fighters[position[0]][position[1]]
        res.append(fighters[position[0]][position[1]])
    return res


def test_random():
    """Should work with random values."""
    for i in range(40):
        moves = []
        for i in range(random.randint(3,50)):
    	    moves.append(random.choice(opts))
        assert street_fighter_selection(fighters,(0,0), moves) == my_street_fighter_selection(fighters,(0,0), moves)
