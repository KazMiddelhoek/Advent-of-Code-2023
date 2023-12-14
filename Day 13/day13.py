with open("Day 13/input.txt") as file:
    fields_together = file.read().splitlines()


def find_symmetry_lines(field):
    possible_mirrors = set(range(1, len(field[0])))
    for row in field:
        for idx, _ in enumerate(row):

            if idx < len(row)*0.5:
                left_of_line = row[:idx]
                right_of_line = row[idx:idx+idx][::-1]
                if left_of_line != right_of_line:
                    possible_mirrors.discard(idx)
            else:
                left_of_line = row[idx-(len(row)-idx):idx] 
                right_of_line = row[idx:][::-1]
                if left_of_line != right_of_line:
                    possible_mirrors.discard(idx)
    return possible_mirrors


# split fields in list of lists:
fields = [[]]
for row in fields_together:
    if row == "" and fields[-1]:
        fields.append([])
        continue
    fields[-1].append(row)

# summary_total = 0
# for field in fields:
#     possible_vertical_mirrors = find_symmetry_lines(field)

#     # transpose field
#     field = list(map(list, zip(*field)))
#     possible_horizontal_mirrors = find_symmetry_lines(field)

#     summary = sum(possible_vertical_mirrors) + 100 * sum(possible_horizontal_mirrors)
#     summary_total+= summary
# print(summary_total)

# part two:
summary_total=0
for field in fields:
    og_possible_vertical_mirrors = find_symmetry_lines(field) # og mirrors
    for idx, _ in enumerate(field):
        field[idx] = list(field[idx])

    found= False
    for row_idx, row in enumerate(field):
        for col_idx, _ in enumerate(row):
            field[row_idx][col_idx] = "." if field[row_idx][col_idx] == "#" else "#"
            new_possible_vertical_mirror = find_symmetry_lines(field)
            field[row_idx][col_idx] = "." if field[row_idx][col_idx] == "#" else "#"

            if new_possible_vertical_mirror and new_possible_vertical_mirror != og_possible_vertical_mirrors:
                found=True
                break
        if found:
            break

    # transpose field
    field = list(map(list, zip(*field)))
    og_possible_horizontal_mirrors = find_symmetry_lines(field)

    found = False
    for row_idx, row in enumerate(field):
        for col_idx, _ in enumerate(row):
                field[row_idx][col_idx] = "." if field[row_idx][col_idx] == "#" else "#"
                new_possible_horizontal_mirror = find_symmetry_lines(field)
                field[row_idx][col_idx] = "." if field[row_idx][col_idx] == "#" else "#"
                if new_possible_horizontal_mirror and new_possible_horizontal_mirror!= og_possible_horizontal_mirrors:
                    found=True
                    break
        if found:
            break

    new_possible_horizontal_mirror = new_possible_horizontal_mirror - og_possible_horizontal_mirrors
    new_possible_vertical_mirror = new_possible_vertical_mirror - og_possible_vertical_mirrors

    summary = sum(new_possible_vertical_mirror) + 100 * sum(new_possible_horizontal_mirror)
    summary_total+= summary
print(summary_total)