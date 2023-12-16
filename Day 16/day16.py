with open("Day 16/input.txt", newline="") as file:
    contraption = file.read().splitlines()

# pad with walls:
contraption = ["#"+row+"#" for row in contraption]
contraption = ["#"*len(contraption[0]), *contraption, "#"*len(contraption[0])]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def find_number_of_energized_tiles(start_position):
    current_positions_and_directions = (start_position,)
    visited_positions_and_directions = set()
    new_positions_and_directions = [start_position]
    while current_positions_and_directions and not all(pos_dir in visited_positions_and_directions for pos_dir in new_positions_and_directions):
        new_positions_and_directions = []
        for position, direction in current_positions_and_directions:
            current_symbol = contraption[position[1]][position[0]]
            if current_symbol == "#":
                continue
            if (position, direction) in visited_positions_and_directions:
                continue

            visited_positions_and_directions.add((position, direction))

            if current_symbol == ".":
                if direction == UP:
                    new_positions_and_directions.append(((position[0], position[1]-1), UP))
                if direction == RIGHT:
                    new_positions_and_directions.append(((position[0]+1, position[1]), RIGHT))
                if direction == DOWN:
                    new_positions_and_directions.append(((position[0], position[1]+1), DOWN))
                if direction == LEFT:
                    new_positions_and_directions.append(((position[0]-1, position[1]), LEFT))

            if current_symbol == "/":
                if direction == UP:
                    new_positions_and_directions.append(((position[0]+1, position[1]), RIGHT))
                if direction == RIGHT:
                    new_positions_and_directions.append(((position[0], position[1]-1), UP))
                if direction == DOWN:
                    new_positions_and_directions.append(((position[0]-1, position[1]), LEFT))
                if direction == LEFT:
                    new_positions_and_directions.append(((position[0], position[1]+1), DOWN))
            if current_symbol == "\\":
                if direction == UP:
                    new_positions_and_directions.append(((position[0]-1, position[1]), LEFT))
                if direction == RIGHT:
                    new_positions_and_directions.append(((position[0], position[1]+1), DOWN))
                if direction == DOWN:
                    new_positions_and_directions.append(((position[0]+1, position[1]), RIGHT))
                if direction == LEFT:
                    new_positions_and_directions.append(((position[0], position[1]-1), UP))

            if current_symbol == "|":
                if direction in (RIGHT, LEFT):
                    new_positions_and_directions.append(((position[0], position[1]-1), UP))
                    new_positions_and_directions.append(((position[0], position[1]+1), DOWN))
                if direction == UP:
                    new_positions_and_directions.append(((position[0], position[1]-1), UP))
                if direction == DOWN:
                    new_positions_and_directions.append(((position[0], position[1]+1), DOWN))

            if current_symbol == "-":
                if direction in (UP, DOWN):
                    new_positions_and_directions.append(((position[0]-1, position[1]), LEFT))
                    new_positions_and_directions.append(((position[0]+1, position[1]), RIGHT))
                if direction == LEFT:
                    new_positions_and_directions.append(((position[0]-1, position[1]), LEFT))
                if direction == RIGHT:
                    new_positions_and_directions.append(((position[0]+1, position[1]), RIGHT))

        current_positions_and_directions = new_positions_and_directions
    
    number_of_unique_positions = len(set(pos for pos, _ in visited_positions_and_directions))

    return number_of_unique_positions

number_of_unique_positions = find_number_of_energized_tiles(((1,1), RIGHT))
print(number_of_unique_positions)

# part two
max_visited_positions = -1
for start_position in range(1, len(contraption[0])-1):
    max_visited_positions = max(max_visited_positions, find_number_of_energized_tiles(((start_position, 1), DOWN)))
    max_visited_positions = max(max_visited_positions,find_number_of_energized_tiles(((start_position, len(contraption)-2), UP)))

for start_position in range(1, len(contraption)-1):
    max_visited_positions = max(max_visited_positions,find_number_of_energized_tiles(((1, start_position), RIGHT)))
    max_visited_positions = max(max_visited_positions, find_number_of_energized_tiles(((len(contraption[0])-1, len(contraption)-2), LEFT)))
print(max_visited_positions)