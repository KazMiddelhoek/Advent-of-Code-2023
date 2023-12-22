with open("Day 22/input.txt", newline="") as file:
    bricks = file.read().splitlines()

bricks =[sorted([int(num) for num in end.split(",")] for end in brick.split("~")) for brick in bricks]
print(bricks)

occupied_positions = set(
    (x,y,z) for brick in bricks for x in range(brick[0][0], brick[1][0]+1) for y in range(brick[0][1], brick[1][1]+1) for z in range(brick[0][2], brick[1][2]+1)
)

# let bricks fall
movement=True
while movement:
    movement=False
    for idx, brick in enumerate(bricks):
        min_z_of_brick = min(brick[0][2], brick[1][2])
        if min_z_of_brick == 1:
            continue
        
        can_move_down = all((x,y,min_z_of_brick-1) not in occupied_positions for x in range(brick[0][0], brick[1][0]+1) for y in range(brick[0][1], brick[1][1]+1))
        if can_move_down:
            movement=True
            occupied_positions -= {(x,y,z) for x in range(brick[0][0], brick[1][0]+1) for y in range(brick[0][1], brick[1][1]+1) for z in range(brick[0][2], brick[1][2]+1)}
            bricks[idx][0][2] -=  1
            bricks[idx][1][2] -=  1
            occupied_positions.update({(x,y,z) for x in range(brick[0][0], brick[1][0]+1) for y in range(brick[0][1], brick[1][1]+1) for z in range(brick[0][2], brick[1][2]+1)})
        
# remove brick and see if any brick can fall down
n_bricks_that_can_be_disintegrated = 0
for idx, brick in enumerate(bricks):
    positions_to_remove ={(x,y,z) for x in range(brick[0][0], brick[1][0]+1) for y in range(brick[0][1], brick[1][1]+1) for z in range(brick[0][2], brick[1][2]+1)}

    occupied_positions -= positions_to_remove

    any_brick_can_move_down = False
    for other_brick in bricks[:idx]+bricks[idx+1:]:
        min_z_of_other_brick = min(other_brick[0][2], other_brick[1][2])
        can_move_down = min_z_of_other_brick != 1 and all((x,y,min_z_of_other_brick-1) not in occupied_positions for x in range(other_brick[0][0], other_brick[1][0]+1) for y in range(other_brick[0][1], other_brick[1][1]+1))
        if can_move_down:
            any_brick_can_move_down = True
            break

    if not any_brick_can_move_down:
        n_bricks_that_can_be_disintegrated+=1

    occupied_positions.update(positions_to_remove)
print(n_bricks_that_can_be_disintegrated)

# part two
import copy
total_n_bricks_that_would_fall = 0
for idx, brick in enumerate(bricks):
    # remove brick
    positions_to_remove ={(x,y,z) for x in range(brick[0][0], brick[1][0]+1) for y in range(brick[0][1], brick[1][1]+1) for z in range(brick[0][2], brick[1][2]+1)}
    occupied_positions -= positions_to_remove

    # simulate falling after disintegration
    movement = True
    bricks_that_fell = set()

    other_bricks = copy.deepcopy(bricks[:idx]+bricks[idx+1:])
    occ_pos_copy = copy.deepcopy(occupied_positions)
    while movement:
        movement= False
        for idx_other_brick, other_brick in enumerate(other_bricks):
            min_z_of_other_brick = min(other_brick[0][2], other_brick[1][2])
            can_move_down = min_z_of_other_brick != 1 and all((x,y,min_z_of_other_brick-1) not in occ_pos_copy for x in range(other_brick[0][0], other_brick[1][0]+1) for y in range(other_brick[0][1], other_brick[1][1]+1))
            if can_move_down:
                bricks_that_fell.add(idx_other_brick)
                movement = True
                occ_pos_copy -= {(x,y,z) for x in range(other_brick[0][0], other_brick[1][0]+1) for y in range(other_brick[0][1], other_brick[1][1]+1) for z in range(other_brick[0][2], other_brick[1][2]+1)}
                other_bricks[idx_other_brick][0][2] -=  1
                other_bricks[idx_other_brick][1][2] -=  1
                occ_pos_copy.update({(x,y,z) for x in range(other_brick[0][0], other_brick[1][0]+1) for y in range(other_brick[0][1], other_brick[1][1]+1) for z in range(other_brick[0][2], other_brick[1][2]+1)})
    total_n_bricks_that_would_fall += len(bricks_that_fell)
    occupied_positions.update(positions_to_remove)

print(total_n_bricks_that_would_fall)