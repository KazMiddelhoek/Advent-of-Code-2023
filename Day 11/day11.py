with open("Day 11/input.txt") as file:
    cosmos = file.read().splitlines()

expanded_cosmos = []
for row in cosmos:
    expanded_cosmos.append(row)
    if all(spot == "." for spot in row):
        expanded_cosmos.append(row)

twice_expanded_cosmos = []

column_idx = 0
while column_idx < len(expanded_cosmos[0]):
    if all(row[column_idx]=="." for row in expanded_cosmos):
        for row_idx, row in enumerate(expanded_cosmos):
            expanded_cosmos[row_idx] = row[:column_idx] + "." + row[column_idx:]
        column_idx+=1
    column_idx+=1

print(expanded_cosmos)
        
# find all galaxies:
galaxy_locs = []
for row_idx, row in enumerate(expanded_cosmos):
    for col_idx, col in enumerate(row):
        if col != ".":
            galaxy_locs.append((row_idx,col_idx))


sum_of_shortest_paths = 0
for loc_idx, loc1 in enumerate(galaxy_locs):
    for loc2 in galaxy_locs[loc_idx+1:]:
        sum_of_shortest_paths += abs(loc1[0] - loc2[0]) + abs(loc1[1] -loc2[1])
print(sum_of_shortest_paths)


# part two
rows_to_expand = []
for idx, row in enumerate(cosmos):
    if all(spot == "." for spot in row):
        rows_to_expand.append(idx)

column_idx = 0
cols_to_expand = []
while column_idx < len(cosmos[0]):
    if all(row[column_idx]=="." for row in cosmos):
        cols_to_expand.append(column_idx)
    column_idx+=1

print(cols_to_expand)
        
# find all galaxies:
galaxy_locs = []
for row_idx, row in enumerate(cosmos):
    for col_idx, col in enumerate(row):
        if col != ".":
            galaxy_locs.append((row_idx,col_idx))


sum_of_shortest_paths = 0
for loc_idx, loc1 in enumerate(galaxy_locs):
    for loc2 in galaxy_locs[loc_idx+1:]:
        sum_of_shortest_paths += (abs(loc1[0] - loc2[0]) + 999_999 * len([row_idx for row_idx in range(min(loc1[0], loc2[0]), max(loc1[0],loc2[0])) if row_idx in rows_to_expand])  
                                + abs(loc1[1] -loc2[1]) + 999_999 * len([col_idx for col_idx in range(min(loc1[1], loc2[1]), max(loc1[1],loc2[1])) if col_idx in cols_to_expand])  )
print(sum_of_shortest_paths)
