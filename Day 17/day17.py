with open("Day 17/test.txt", newline="") as file:
    map = file.read().splitlines()
import math
# pad with walls:
map = ["#"+row+"#" for row in map]
map = ["#"*len(map[0]), *map, "#"*len(map[0])]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

visited_locs = set()
visited_locs_location_only = set()

position = (1+1j, RIGHT, 1)

shortest_distances = {(i+k*1j, direction, conseq) : math.inf for i in range(1, len(map)-1) for k in range(1, len(map[0])-1) for direction in (UP, RIGHT, DOWN, LEFT) for conseq in range(1,4) if (i+k*1j) != (1,1)}
shortest_distances[(1+1j, RIGHT, 1)] = 0
shortest_distances[(1+1j, DOWN, 1)] = 0
unvisited_locs = shortest_distances.copy()

i=0
end_point =len(map[0])-2 + (len(map)-2)*1j
while end_point not in visited_locs_location_only:
    if not i%100:
        print(i)
    i+=1
    if position[1] == RIGHT:
        neighbor_nodes = [
            (position[0]-1j,UP,1),
            (position[0]+1,RIGHT,position[2]+1),
            (position[0]+1j,DOWN,1),
        ]
    elif position[1] == DOWN:
        neighbor_nodes = [
            (position[0]-1,LEFT,1),
            (position[0]+1,RIGHT,1),
            (position[0]+1j,DOWN,position[2]+1),
        ]        
    elif position[1] == LEFT:
        neighbor_nodes = [
            (position[0]-1,LEFT,position[2]+1),
            (position[0]-1j,UP,1),
            (position[0]+1j,DOWN,1),
        ]         
    elif position[1] == UP:
        neighbor_nodes = [
            (position[0]-1,LEFT,1),
            (position[0]-1j,UP,position[2]+1),
            (position[0]+1,RIGHT,1),
        ]         

    # filter possible neighbors
    neighbor_nodes = [neighbor for neighbor in neighbor_nodes if map[int(neighbor[0].imag)][int(neighbor[0].real)] != "#" and neighbor[2] < 4]
    neighbor_nodes = [neighbor for neighbor in neighbor_nodes if not any((neighbor[0], neighbor[1], poss) in visited_locs for poss in range(1,neighbor[2]+1))]

    for neighbor in neighbor_nodes:
        shortest_distances[neighbor] = min(shortest_distances[neighbor], shortest_distances[position] + int(map[int(neighbor[0].imag)][int(neighbor[0].real)]))
        unvisited_locs[neighbor] = shortest_distances[neighbor]

    unvisited_locs.pop(position)
    visited_locs.add(position)
    visited_locs_location_only.add(position[0])
    
    position = min({k:v for k, v in shortest_distances.items() if k in unvisited_locs}, key=shortest_distances.get)

end_point_reached ={k:v for k, v in shortest_distances.items() if k[0] == end_point}
print(end_point_reached[min(end_point_reached, key=end_point_reached.get)])

