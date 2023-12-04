from __future__ import annotations
with open("Day 03/input.txt") as file:
    rows = file.read().splitlines()

def is_adjacent_to_symbol(rows: list[str], row_idx: int, col_idx:int):
    for surrounding_row in range(-1, 2):
        for surrounding_col in range(-1, 2):
            if (
                (row_idx == 0 and surrounding_row == -1) or 
                (row_idx == len(rows)-1 and surrounding_row == 1) or
                (col_idx == 0 and surrounding_col == -1) or 
                (col_idx == len(rows[0])-1 and surrounding_col == 1)
            ):
                continue

            if (not rows[row_idx+surrounding_row][col_idx+surrounding_col].isnumeric() and 
                rows[row_idx+surrounding_row][col_idx+surrounding_col] != "."):
                return True
    
    return False

sum_of_part_numbers = 0
for row_idx, row in enumerate(rows):
    current_number = ""
    number_is_adjacent_to_symbol = False
    for col_idx, char in enumerate(row):
        if char.isdigit():
            current_number += char
            if is_adjacent_to_symbol(rows, row_idx, col_idx):
                number_is_adjacent_to_symbol = True
            if col_idx < len(row)-1:
                continue
        
        if current_number.isdigit() and number_is_adjacent_to_symbol:
            sum_of_part_numbers += int(current_number)
    
        current_number=""
        number_is_adjacent_to_symbol = False

print(sum_of_part_numbers)

# part two

with open("Day 03/input.txt") as file:
    rows = file.read().splitlines()

def adjacent_multiplicaton_symbols(rows: list[str], row_idx: int, col_idx:int):
    locations = set()
    for surrounding_row in range(-1, 2):
        for surrounding_col in range(-1, 2):
            if (
                (row_idx == 0 and surrounding_row == -1) or 
                (row_idx == len(rows)-1 and surrounding_row == 1) or
                (col_idx == 0 and surrounding_col == -1) or 
                (col_idx == len(rows[0])-1 and surrounding_col == 1)
            ):
                continue

            if (rows[row_idx+surrounding_row][col_idx+surrounding_col] == "*"):
                locations.add((row_idx+surrounding_row, col_idx + surrounding_col))
    return locations

multiplication_to_numbers = {}
for row_idx, row in enumerate(rows):
    current_number = ""
    multiplication_symbols = set()
    for col_idx, char in enumerate(row):
        if char.isdigit():
            current_number += char
            multiplication_symbols.update(adjacent_multiplicaton_symbols(rows, row_idx, col_idx))
            if col_idx < len(row)-1:
                continue
        
        if current_number.isdigit():
            for symbol in multiplication_symbols:
                multiplication_to_numbers[symbol] = multiplication_to_numbers.get(symbol, []) + [int(current_number)]
    
        current_number=""
        multiplication_symbols = set()

sum_of_part_numbers = sum(numbers[0] * numbers[1] for numbers in multiplication_to_numbers.values() if len(numbers) == 2)
print(sum_of_part_numbers)