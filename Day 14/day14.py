with open("Day 14/input.txt") as file:
    platform = file.read().splitlines()
import copy
platform = [list(row) for row in platform]

movement_is_happening = True
while movement_is_happening:
    old_platform = copy.deepcopy(platform)
    for row_idx, row in enumerate(platform[1:],1):
        for col_idx, char in enumerate(row):
            if char == "O" and platform[row_idx-1][col_idx] ==".":
                platform[row_idx-1][col_idx]="O"
                platform[row_idx][col_idx] ="."
    
    movement_is_happening = platform != old_platform

total_load = 0
for row_idx_from_south, row in enumerate(platform[::-1],1):
    for char in row:
        if char == "O":
            total_load+= row_idx_from_south
print(total_load)

# part two
import math
platform = [list(row) for row in platform]
seen_platforms = dict()
i=0
while i < 1_000_000_000:
    tuple_platform = tuple(tuple(row) for row in platform)
    print(i)
    if tuple_platform in seen_platforms:
        add = math.floor((1_000_000_000 - i) /(i - seen_platforms[tuple_platform] ))
        i += add*(i - seen_platforms[tuple_platform] )
        print("gotcha")

    seen_platforms[tuple_platform] = i
    # north
    movement_is_happening=True
    while movement_is_happening:
        old_platform = copy.deepcopy(platform)
        for row_idx, row in enumerate(platform[1:],1):
            for col_idx, char in enumerate(row):
                if char == "O" and platform[row_idx-1][col_idx] ==".":
                    platform[row_idx-1][col_idx]="O"
                    platform[row_idx][col_idx] ="."
        movement_is_happening = platform != old_platform
    # west
    movement_is_happening=True
    while movement_is_happening:
        old_platform = copy.deepcopy(platform)
        for row_idx, row in enumerate(platform):
            for col_idx, char in enumerate(row[1:], 1):
                if char == "O" and platform[row_idx][col_idx-1] ==".":
                    platform[row_idx][col_idx-1]="O"
                    platform[row_idx][col_idx] ="."
        movement_is_happening = platform != old_platform

    # south
    movement_is_happening=True
    while movement_is_happening:
        old_platform = copy.deepcopy(platform)
        for row_idx, row in enumerate(platform[:-1]):
            for col_idx, char in enumerate(row):
                if char == "O" and platform[row_idx+1][col_idx] ==".":
                    platform[row_idx+1][col_idx]="O"
                    platform[row_idx][col_idx] ="."
        movement_is_happening = platform != old_platform

    # east
    movement_is_happening=True
    while movement_is_happening:
        old_platform = copy.deepcopy(platform)
        for row_idx, row in enumerate(platform):
            for col_idx, char in enumerate(row[:-1]):
                if char == "O" and platform[row_idx][col_idx+1] ==".":
                    platform[row_idx][col_idx+1]="O"
                    platform[row_idx][col_idx] ="."    
        movement_is_happening = platform != old_platform

    i+= 1

total_load = 0
for row_idx_from_south, row in enumerate(platform[::-1],1):
    for char in row:
        if char == "O":
            total_load += row_idx_from_south
print(total_load)
