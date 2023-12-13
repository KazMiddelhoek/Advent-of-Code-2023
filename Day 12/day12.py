from itertools import combinations

# with open("Day 12/input.txt") as file:
#     field = file.read().splitlines()

# def is_possible_arrangement(row, wanted_groups):
#     counts_of_damaged_spings = [len(springs) for springs in filter(lambda x: len(x) > 0, row.split("."))]
#     return counts_of_damaged_spings == wanted_groups

# sum_of_possible_arrangements = 0
# for row in field:
#     possible_arrangements = 0 
#     row, wanted_groups = row.split()
#     wanted_groups = [int(group) for group in wanted_groups.split(",")]
#     number_of_damaged_springs = len([char for char in row if char == "#"])
#     springs_to_add = sum(wanted_groups) - number_of_damaged_springs
#     question_mark_locs = [idx for idx, char in enumerate(row) if char == "?"]

#     for possible_order in combinations(question_mark_locs, springs_to_add):
#         potential_row = list(row)
#         for idx in possible_order:
#             potential_row[idx] = "#"
        
#         potential_row = "".join(potential_row).replace("?", ".")
        
#         if is_possible_arrangement(potential_row, wanted_groups):
#             possible_arrangements += 1
#     sum_of_possible_arrangements += possible_arrangements
# print(sum_of_possible_arrangements)

# part two
with open("Day 12/test.txt") as file:
    field = file.read().splitlines()

from functools import lru_cache

@lru_cache(None)
def is_possible_arrangement(row: str, wanted_groups, current_pos: int, possible_arrangements, groups_so_far):
    wanted_groups_so_far = wanted_groups[:len(groups_so_far)]

    possible_arrangements=0
    if groups_so_far and wanted_groups_so_far and (groups_so_far[:-1] != wanted_groups_so_far[:-1] or groups_so_far[-1] > wanted_groups_so_far[-1]):
        return possible_arrangements

    for current_pos, char in enumerate(row[current_pos:], current_pos):
        if char !="?":
            continue
        groups_so_far = tuple(len(group) for group in row[:current_pos].replace("."," ").split())
        possible_arrangements+=is_possible_arrangement(row[:current_pos] + "#" + row[current_pos+1:], wanted_groups, current_pos+1, possible_arrangements, groups_so_far)
        possible_arrangements+=is_possible_arrangement(row[:current_pos] + "." + row[current_pos+1:], wanted_groups, current_pos+1, possible_arrangements, groups_so_far)
        return possible_arrangements

    if current_pos == len(row) - 1 and "?" not in row:
        counts_of_damaged_spings = tuple(len(group) for group in row.replace("."," ").split())
        if counts_of_damaged_spings == wanted_groups:
            return possible_arrangements+1
        else:
            return possible_arrangements

    return possible_arrangements



sum_of_possible_arrangements = 0
for row in field:
    row, wanted_groups = row.split()
    wanted_groups = [int(group) for group in wanted_groups.split(",")] 

    row = "?".join([row] * 5) +"."
    wanted_groups = tuple(wanted_groups * 5)
    groups_so_far = tuple()

    possible_arrangements = is_possible_arrangement(row, wanted_groups, 0, 0, groups_so_far)
    sum_of_possible_arrangements += possible_arrangements
    print(possible_arrangements)

       
print(sum_of_possible_arrangements)