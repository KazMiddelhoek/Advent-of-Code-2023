with open("Day 23/input.txt", newline="") as file:
    map = file.read().splitlines()

PATH = "."
FOREST ="#"
SLOPE_UP = "^"
SLOPE_RIGHT =">"
SLOPE_DOWN ="v"
SLOPE_LEFT = "<"

current_positions = (1,0)
end_pos = (len(map[0])-2 ,len(map)-1)

steps_taken = []

import sys
sys.setrecursionlimit(5000)

def walk(position, distance_travelled, path_taken: set):
    distance_travelled+=1
    path_taken.add(position)
    if position == end_pos:
        steps_taken.append(distance_travelled)
        path_taken.remove(position)
        return

    left = (position[0]-1, position[1])
    right = (position[0]+1, position[1])
    up = (position[0], position[1]-1)
    down = (position[0], position[1]+1)

    if map[left[1]][left[0]] in (PATH, SLOPE_LEFT) and left not in path_taken:
        walk(left, distance_travelled,path_taken)
    if map[right[1]][right[0]] in (PATH, SLOPE_RIGHT) and right not in path_taken:
        walk(right,distance_travelled,path_taken)
    if map[up[1]][up[0]] in (PATH, SLOPE_UP) and up not in path_taken:
        walk(up, distance_travelled,path_taken)
    if map[down[1]][down[0]] in (PATH, SLOPE_DOWN) and down not in path_taken:
        walk(down, distance_travelled,path_taken)
    
    path_taken.remove(position)

path_taken = set()
walk(current_positions, -1, path_taken)
print(max(steps_taken))

# part two
current_positions = (1,0)
end_pos = (len(map[0])-2 ,len(map)-1)

steps_taken = []

path_types = (PATH, SLOPE_LEFT, SLOPE_UP, SLOPE_RIGHT, SLOPE_DOWN)

def draw_path_taken(total_path_taken):
    s = "" 
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (x,y) in total_path_taken:
                s+="O"
            else:
                s+=map[y][x]
        s+="\n"
    with open("testoutput.txt", "w") as f:
        f.write(s)

def walk(position, distance_travelled, total_path_taken: set):
    path_list = set()

    teleported = False
    if position in teleporter:
        path_list.update(teleporter[position][1])
        total_path_taken.update(teleporter[position][1])
        distance_travelled += len(teleporter[position][1])-1
        position = teleporter[position][0]
        teleported = True
    
    start_pos = position
    previous_position = False
    only_one_option = True
    while only_one_option:
        path_list.add(position)
        total_path_taken.add(position)

        if position == end_pos:
            steps_taken.append(distance_travelled)
            total_path_taken -= set(path_list)
            return

        left = (position[0]-1, position[1])
        right = (position[0]+1, position[1])
        up = (position[0], position[1]-1)
        down = (position[0], position[1]+1)
        
        directions_to_go = []
        for direction in [left, right, up, down]:
            if map[direction[1]][direction[0]] in path_types and direction not in total_path_taken:
                directions_to_go.append(direction)

        only_one_option = len(directions_to_go) == 1
        dead_end = len(directions_to_go) == 0

        if only_one_option:
            distance_travelled+=1
            previous_position = position
            position=directions_to_go[0]   
        
        if not only_one_option and not dead_end and previous_position:
            if not teleported:
                path_without_current = path_list.copy()
                path_without_current.remove(position)
                teleporter[start_pos] = [previous_position, path_without_current]
                teleporter[previous_position] = [start_pos, path_without_current]
        
    for direction in directions_to_go:
        walk(direction, distance_travelled+1, total_path_taken)

    total_path_taken -= path_list
    return

teleporter = {}
total_path_taken = set()
steps_taken = []
walk(current_positions, 0, total_path_taken)
print(steps_taken)
print(max(steps_taken))
