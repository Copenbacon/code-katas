def street_fighter_selection(fighters, initial_position, moves):
    dict_of_fighters = {
        (0, 0): "Ryu",
        (0, 1): "E.Honda",
        (0, 2): "Blanka",
        (0, 3): "Guile",
        (0, 4): "Balrog",
        (0, 5): "Vega",
	    (1, 0): "Ken",
        (1, 1): "Chun Li",
        (1, 2): "Zangief",
        (1, 3): "Dhalsim",
        (1, 4): "Sagat",
        (1,5): "M.Bison"
    }
    solution = []
    num_of_moves = len(moves)
    for move in moves:
        if move == "left":
            initial_position = (initial_position[0], initial_position[1]-1)
            if initial_position[1] < 0:
                initial_position = (initial_position[0], 5)
        if move == "right":
            initial_position = (initial_position[0], initial_position[1]+1)
            if initial_position[1] > 5:
                initial_position = (initial_position[0], 0)
        if move == "up":
            initial_position = (initial_position[0] - 1, initial_position[1])
            if initial_position[0] < 0:
                initial_position = (0, initial_position[1])
        if move == "down":
            initial_position = (initial_position[0] + 1, initial_position[1])
            if initial_position[0] > 1:
                initial_position = (1, initial_position[1])
        solution.append(dict_of_fighters[initial_position])
    return solution