from __future__ import annotations

with open("Day 10/input.txt") as file:
    rows = file.read().splitlines()

# find starting position
for y, row in enumerate(rows):
    x = row.find("S")
    if x != -1:
        start_position = (x, y)
        break

# 0 is up, 1 is right, 2 is down, 3 is left
def new_position_and_direction(current_position, current_direction):
    if current_direction == 0:
        new_position = (current_position[0], current_position[1] -1)
        if rows[new_position[1]][new_position[0]] == "|":
            return [new_position,current_direction]
        elif rows[new_position[1]][new_position[0]] == "7":
            return [new_position,3]
        elif rows[new_position[1]][new_position[0]] == "F":
            return [new_position,1]
        
    if current_direction == 1:
        new_position = (current_position[0]+1, current_position[1])

        if rows[new_position[1]][new_position[0]] == "-":
            return [new_position, 1]
        elif rows[new_position[1]][new_position[0]] == "J":
            return [new_position,0]
        elif rows[new_position[1]][new_position[0]] == "7":
            return [new_position,2]
        
    if current_direction == 2:
        new_position = (current_position[0], current_position[1]+1)
        if rows[new_position[1]][new_position[0]] == "|":
            return [new_position, 2]
        elif rows[new_position[1]][new_position[0]] == "J":
            return [new_position,3]
        elif rows[new_position[1]][new_position[0]] == "L":
            return [new_position,1]
        
    if current_direction == 3:
        new_position = (current_position[0]-1, current_position[1])
        if rows[new_position[1]][new_position[0]] == "-":
            return [new_position, 3]
        elif rows[new_position[1]][new_position[0]] == "F":
            return [new_position,2]
        elif rows[new_position[1]][new_position[0]] == "L":
            return [new_position,0]       
    return None

current_positions=[[start_position, i] for i in range(4)]

steps_taken = 0
while len(current_positions) != 2 or not (current_positions[0][0] == current_positions[1][0]):
    for position_idx, position in enumerate(current_positions):
        current_positions[position_idx] = new_position_and_direction(position[0], position[1])
    current_positions = [pos for pos in current_positions if pos is not None]
    steps_taken +=1
print(steps_taken)


# part two
with open("Day 10/input.txt") as file:
    rows = file.read().splitlines()

for y, row in enumerate(rows):
    x = row.find("S")
    if x != -1:
        start_position = (x, y)
        break

loop_tiles=[[start_position, 0]]
while len(loop_tiles)<2 or loop_tiles[-1] is not None:
    loop_tiles.append(new_position_and_direction(loop_tiles[-1][0], loop_tiles[-1][1]))
print(loop_tiles)
loop_tiles=loop_tiles[:-1] # remove None
loop_tiles = { tile[0] for tile in loop_tiles}

n_enclosed = 0
for y in range(len(rows)):
    inside = False

    for x in range(len(rows[0])):
        if (x,y) in loop_tiles and rows[y][x] in "|JLS":
            inside = not inside

        if inside and (x,y) not in loop_tiles:
            n_enclosed+=1
print(n_enclosed)





            