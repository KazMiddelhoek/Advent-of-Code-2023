with open("Day 21/input.txt", newline="") as file:
    map = file.read().splitlines()

garden_plots = set()
rocks = set()
current_positions = set()

for row, line in enumerate(map):
    for col, spot in enumerate(line):
        if spot == "#":
            rocks.add((col, row))
        elif spot == ".":
            garden_plots.add((col,row))
        elif spot == "S":
            current_positions.add((col,row))
            garden_plots.add((col,row))

for step in range(64):
    new_positions = set()
    for position in current_positions:
        new_possible_positions= [
            (position[0]-1, position[1]),
            (position[0]+1, position[1]),
            (position[0], position[1]-1),
            (position[0], position[1]+1),
        ]
        new_possible_positions = [pos for pos in new_possible_positions if pos in garden_plots]
        new_positions.update(new_possible_positions)
    current_positions = new_positions
print(len(current_positions))

# part two

