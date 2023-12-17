import math
import heapq

with open("Day 17/input.txt", newline="") as file:
    city = file.read().splitlines()

# pad with walls:
city = ["#"+row+"#" for row in city]
city = ["#"*len(city[0]), *city, "#"*len(city[0])]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

visited_locs = set()
visited_locs_location_only = set()

position = ((1,1), RIGHT, 0)
shortest_distances = {((i,k), direction, conseq) : math.inf for i in range(1, len(city)-1) for k in range(1, len(city[0])-1) for direction in (UP, RIGHT, DOWN, LEFT) for conseq in range(1,4)}
for dir in [UP, RIGHT, DOWN, LEFT]:
    shortest_distances[((1,1), dir, 0)] = 0

positions_to_check = [(0, position)]
heapq.heapify(positions_to_check)
unvisited_locs = shortest_distances.copy()

end_point = (len(city[0])-2 ,len(city)-2)
while end_point not in visited_locs_location_only:
    position = heapq.heappop(positions_to_check)[1]
    if position[1] == RIGHT:
        neighbor_nodes = [
            ((position[0][0], position[0][1]-1),UP,1),
            ((position[0][0]+1, position[0][1]),RIGHT,position[2]+1),
            ((position[0][0], position[0][1]+1),DOWN,1),
        ]
    elif position[1] == DOWN:
        neighbor_nodes = [
            ((position[0][0]-1, position[0][1]),LEFT,1),
            ((position[0][0]+1, position[0][1]),RIGHT,1),
            ((position[0][0], position[0][1]+1),DOWN, position[2]+1),
        ]        
    elif position[1] == LEFT:
        neighbor_nodes = [
            ((position[0][0]-1, position[0][1]),LEFT,position[2]+1),
            ((position[0][0], position[0][1]-1),UP,1),
            ((position[0][0], position[0][1]+1),DOWN,1),
        ]         
    elif position[1] == UP:
        neighbor_nodes = [
            ((position[0][0]-1, position[0][1]),LEFT,1),
            ((position[0][0], position[0][1]-1),UP,position[2]+1),
            ((position[0][0]+1, position[0][1]),RIGHT,1),
        ]         

    # filter possible neighbors
    neighbor_nodes = [neighbor for neighbor in neighbor_nodes if city[int(neighbor[0][1])][int(neighbor[0][0])] != "#" and neighbor[2] < 4]
    neighbor_nodes = [neighbor for neighbor in neighbor_nodes if not any((neighbor[0], neighbor[1], poss) in visited_locs for poss in range(1,neighbor[2]+1))]

    for neighbor in neighbor_nodes:
        heat_of_neighbor = int(city[int(neighbor[0][1])][int(neighbor[0][0])])
        if shortest_distances[position] + heat_of_neighbor < shortest_distances[neighbor]:
            shortest_distances[neighbor] = shortest_distances[position] + heat_of_neighbor
            heapq.heappush(positions_to_check,(shortest_distances[neighbor], neighbor))
        unvisited_locs[neighbor] = shortest_distances[neighbor]

    unvisited_locs.pop(position)
    visited_locs.add(position)
    visited_locs_location_only.add(position[0])

end_point_reached ={k:v for k, v in shortest_distances.items() if k[0] == end_point}
print(end_point_reached[min(end_point_reached, key=end_point_reached.get)])

# part two
transposed_city = list(map(list, zip(*city)))

visited_locs = set()
visited_locs_location_only = set()

position = ((1,1), RIGHT, 0)
shortest_distances = {((i,k), direction, conseq) : math.inf for i in range(1, len(city)-1) for k in range(1, len(city[0])-1) for direction in (UP, RIGHT, DOWN, LEFT) for conseq in range(1,11)}
for dir in [UP, RIGHT, DOWN, LEFT]:
    shortest_distances[((1,1), dir, 0)] = 0

positions_to_check = [(0, position)]
heapq.heapify(positions_to_check)
unvisited_locs = shortest_distances.copy()

end_point = (len(city[0])-2 ,len(city)-2)
while end_point not in visited_locs_location_only:
    position = heapq.heappop(positions_to_check)[1]
    if position[1] == RIGHT:
        neighbor_nodes = [
            *[((position[0][0], position[0][1]-i),UP,i) for i in range(4,11)],
            *[((position[0][0]+i, position[0][1]),RIGHT,position[2]+i) for i in range(4,11)],
            *[((position[0][0], position[0][1]+i),DOWN,i) for i in range(4,11)],
        ]
    elif position[1] == DOWN:
        neighbor_nodes = [
            *[((position[0][0]-i, position[0][1]),LEFT,i) for i in range(4,11)],
            *[((position[0][0]+i, position[0][1]),RIGHT,i) for i in range(4,11)],
            *[((position[0][0], position[0][1]+i),DOWN, position[2]+i) for i in range(4,11)],
        ]        
    elif position[1] == LEFT:
        neighbor_nodes = [
            *[((position[0][0]-i, position[0][1]),LEFT,position[2]+i) for i in range(4,11)],
            *[((position[0][0], position[0][1]-i),UP,i) for i in range(4,11)],
            *[((position[0][0], position[0][1]+i),DOWN,i) for i in range(4,11)],
        ]         
    elif position[1] == UP:
        neighbor_nodes = [
            *[((position[0][0]-i, position[0][1]),LEFT,i) for i in range(4,11)],
            *[((position[0][0], position[0][1]-i),UP,position[2]+i) for i in range(4,11)],
            *[((position[0][0]+i, position[0][1]),RIGHT,i) for i in range(4,11)],
        ]         

    # filter possible neighbors
    neighbor_nodes = [neighbor for neighbor in neighbor_nodes if 1 <= neighbor[0][0] <= len(city[0])-2 and 1 <= neighbor[0][1] <= len(city)-2  and 3 < neighbor[2] < 11]
    neighbor_nodes = [neighbor for neighbor in neighbor_nodes if neighbor not in visited_locs]

    for neighbor in neighbor_nodes:
        if neighbor[0][1] == position[0][1]:
            if neighbor[0][0] > position[0][0]:
                numbers = list(city[position[0][1]][int(position[0][0])+1:int(neighbor[0][0])+1])
            else:
                numbers = list(city[position[0][1]][int(neighbor[0][0]):int(position[0][0])])
            numbers = [int(n) for n in numbers]
            heat_of_neighbor = sum(numbers)
        else:
            if neighbor[0][1] > position[0][1]:
                numbers = list(transposed_city[position[0][0]][int(position[0][1])+1:int(neighbor[0][1])+1])
            else:
                numbers = list(transposed_city[position[0][0]][int(neighbor[0][1]):int(position[0][1])])
            numbers = [int(n) for n in numbers]
            heat_of_neighbor = sum(numbers)

        if shortest_distances[position] + heat_of_neighbor < shortest_distances[neighbor]:
            shortest_distances[neighbor] = shortest_distances[position] + heat_of_neighbor
            heapq.heappush(positions_to_check,(shortest_distances[neighbor], neighbor))
        unvisited_locs[neighbor] = shortest_distances[neighbor]

    if position in unvisited_locs:
        unvisited_locs.pop(position)
    visited_locs.add(position)
    visited_locs_location_only.add(position[0])

end_point_reached ={k:v for k, v in shortest_distances.items() if k[0] == end_point}
print(end_point_reached[min(end_point_reached, key=end_point_reached.get)])