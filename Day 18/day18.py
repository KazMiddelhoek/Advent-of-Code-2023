with open("Day 18/input.txt", newline="") as file:
    dig_plan = file.read().splitlines()

current_pos = (0,0)
trench = set((current_pos,))

for instruction in dig_plan:
    direction, distance, color =instruction.split()
    distance = int(distance)
    if direction == "R":
        for i in range(1, distance+1):
            current_pos = (current_pos[0]+1, current_pos[1])
            trench.add(current_pos)
    
    elif direction == "D":
        for i in range(1, distance+1):
            current_pos = (current_pos[0], current_pos[1]+1)
            trench.add(current_pos)

    elif direction == "L":
        for i in range(1, distance+1):
            current_pos = (current_pos[0]-1, current_pos[1])
            trench.add(current_pos)
    
    elif direction == "U":
        for i in range(1, distance+1):
            current_pos = (current_pos[0], current_pos[1]-1)
            trench.add(current_pos)

max_x = max(trench, key=lambda x: x[0])[0]
min_x = min(trench, key=lambda x: x[0])[0]
min_y = min(trench, key=lambda x: x[1])[1]
max_y = max(trench, key=lambda x: x[1])[1]
string = ""

start_pos = (11, -7)
neighbours = set((start_pos,))
filled_cubes = set((start_pos,))

i = 0
while neighbours or i<10000:
    i+=1
    new_neighbour_set = set()
    for neighbour in neighbours:
        new_neighbours = [
            (neighbour[0]-1, neighbour[1]),
            (neighbour[0]+1, neighbour[1]),
            (neighbour[0], neighbour[1]-1),
            (neighbour[0], neighbour[1]+1),
        ]
        for new_neighbour in new_neighbours:
            if new_neighbour not in trench and new_neighbour not in filled_cubes:
                filled_cubes.add(new_neighbour)
                new_neighbour_set.add(new_neighbour)
    neighbours = new_neighbour_set

for j in range(min_y, max_y+1):
    for i in range(min_x, max_x+1):
        if (i,j) in trench:
            string+="#"
        elif (i,j) in filled_cubes:
            string+="O"
        else:
            string+="."
    string+="\n"

with open("testoutput.txt", "w") as f:
    f.write(string)

print(len(trench)+len(filled_cubes))

# part two
with open("Day 18/input.txt", newline="") as file:
    dig_plan = file.read().splitlines()

current_pos = (0,0)
trench_corners = [current_pos,]

number_to_direction = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}

for instruction in dig_plan:
    hexadecimal =instruction.split()[-1]
    distance = int(hexadecimal[2:7], 16)
    direction = number_to_direction[hexadecimal[-2]]
    if direction == "R":
        current_pos = (current_pos[0]+distance, current_pos[1])
        trench_corners.append(current_pos)
    elif direction == "D":
            current_pos = (current_pos[0], current_pos[1]+distance)
            trench_corners.append(current_pos)
    elif direction == "L":
            current_pos = (current_pos[0]-distance, current_pos[1])
            trench_corners.append(current_pos)
    elif direction == "U":
            current_pos = (current_pos[0], current_pos[1]-distance)
            trench_corners.append(current_pos)

import math
shoelace = [(y1+y2)*(x1-x2) for (x1, y1), (x2, y2) in zip(trench_corners[:-1], trench_corners[1:])]
area = (sum(shoelace))/2
print(area )
lines = [(x1, x2) for x1, x2 in zip(trench_corners[:-1], trench_corners[1:])]
lines = [sorted(line, key=lambda x: x[0]) for line in lines]
perimeter = sum([math.sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2) for x1, x2 in lines])
print(area + perimeter/2 +1)
