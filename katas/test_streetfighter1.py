import pytest
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

test.it("should go up 4 times, always the same")
moves =  ["up"]*4
solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should go down 4 times, always the same")
moves =  ["down"]*4
solution = ['Ken', 'Ken', 'Ken', 'Ken']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should use all 4 directions counter-clockwise twice")
moves =  ["down","right","up","left"]*2
solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should use all 4 directions clockwise twice")
moves =  ["up","left","down","right"]*2
solution = ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should cover all characters")
moves =  ["up"]+["left"]*6+["down"]+["right"]*6
solution = ['Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Ken']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

import random
test.describe("Random Tests now!")
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
    
test.it("should work with random values")
for i in range(40):
    moves = []
    for i in range(random.randint(3,50)):
	    moves.append(random.choice(opts))
    test.assert_equals(street_fighter_selection(fighters,(0,0), moves), my_street_fighter_selection(fighters,(0,0), moves))

