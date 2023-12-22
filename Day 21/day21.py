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
from collections import defaultdict
from functools import lru_cache

garden_plots = set()
rocks = set()
current_positions = defaultdict(set)

for row, line in enumerate(map):
    for col, spot in enumerate(line):
        if spot == "#":
            rocks.add((col, row))
        elif spot == ".":
            garden_plots.add((col,row))
        elif spot == "S":
            current_positions[(col,row)] = set([(0,0)])
            garden_plots.add((col,row))

map_length = len(map)
map_width = len(map[0])
MOVE_UP = 0
MOVE_RIGHT = 1
MOVE_DOWN = 2
MOVE_LEFT = 3
DONT_MOVE = 4

@lru_cache(None)
def get_new_positions_after_step(position):
    new_positions = set()
    new_possible_positions= [
        (position[0]-1, position[1]),
        (position[0]+1, position[1]),
        (position[0], position[1]-1),
        (position[0], position[1]+1),
    ]
    for new_pos in new_possible_positions:
        if new_pos in rocks:
            continue
        if new_pos[0] == -1:
            new_positions.add(((map_width-1, new_pos[1]),MOVE_LEFT))
        elif new_pos[0] == map_width:
            new_positions.add(((0, new_pos[1]),MOVE_RIGHT))
        elif new_pos[1] == -1:
            new_positions.add(((new_pos[0], map_length-1),MOVE_UP))
        elif new_pos[1] == map_length:
            new_positions.add(((new_pos[0], 0),MOVE_DOWN))       
        else:
            new_positions.add((new_pos, DONT_MOVE))
    return new_positions

visited_positions = set()        

data_points = []
for step in range(1,501):
    new_positions=defaultdict(set)
    for position in current_positions:
        possible_positions = get_new_positions_after_step(position)
    
        for possible_pos, shift in possible_positions:
            if shift==DONT_MOVE:
                new_positions[possible_pos]=new_positions[possible_pos].union(current_positions[position])
            elif shift==MOVE_LEFT:
                new_positions[possible_pos]=new_positions[possible_pos].union([(x-1,y) for x,y in current_positions[position]])
            elif shift==MOVE_RIGHT:
                new_positions[possible_pos]=new_positions[possible_pos].union([(x+1,y) for x,y in current_positions[position]])
            elif shift==MOVE_DOWN:
                new_positions[possible_pos]=new_positions[possible_pos].union([(x,y+1) for x,y in current_positions[position]])
            elif shift==MOVE_UP:
                new_positions[possible_pos]=new_positions[possible_pos].union([(x,y-1) for x,y in current_positions[position]])
    current_positions=new_positions

    if step in (65,65+map_width,65+2*map_width):
        data_points.append((step, sum(len(positions) for positions in current_positions.values())))
        print(data_points[-1])

import plotly.express as px
print(step, sum(len(positions) for positions in current_positions.values()))
fig = px.scatter(x=[x[0] for x in data_points], y=[x[1]for x in data_points])
fig.show()

import numpy as np
points = [(i, data_points[i][1]) for i in range(3)]

def evaluate_quadratic_equation(points, x):
    # Fit a quadratic polynomial (degree=2) through the points
    coefficients = np.polyfit(*zip(*points), 2)

    # Evaluate the quadratic equation at the given x value
    result = np.polyval(coefficients, x)
    return round(result)

print(evaluate_quadratic_equation(points, 202300))
