# with open("Day 05/input.txt") as file:
#     lines = file.read().splitlines()

# numbers_to_convert = [int(number) for number in lines[0].split(": ")[1].split()]

# new_numbers_to_convert = []
# converted_numbers = []
# for conversion_line in lines[2:]:
#     if conversion_line == "":
#         new_numbers_to_convert += [number for number in numbers_to_convert if number not in converted_numbers]
#         numbers_to_convert = new_numbers_to_convert
#         new_numbers_to_convert = []
#         converted_numbers = []
#         continue

#     if not conversion_line[0].isdigit():
#         continue
        
#     destination_range_start, source_range_start, range_length = [int(n) for n in conversion_line.split()]
#     for number in numbers_to_convert:
#         if source_range_start <= number <= source_range_start + range_length:
#             new_numbers_to_convert += [destination_range_start + number - source_range_start]
#             converted_numbers += [number]
# print(min(numbers_to_convert))


# part two
with open("Day 05/input.txt") as file:
    lines = file.read().splitlines()

numbers_to_convert = [int(number) for number in lines[0].split(": ")[1].split()]
number_ranges_to_convert = [(range_start, range_length) for range_start, range_length in zip(numbers_to_convert[::2], numbers_to_convert[1::2])]

new_number_ranges_to_convert = []
converted_numbers = []
for conversion_line in lines[2:]:
    if conversion_line == "":
        new_number_ranges_to_convert += [number for number in number_ranges_to_convert if number[0] not in [i[0] for i in converted_numbers]]
        number_ranges_to_convert = new_number_ranges_to_convert
        new_number_ranges_to_convert = []
        converted_numbers = []
        continue

    if not conversion_line[0].isdigit():
        continue
        
    destination_range_start, source_range_start, range_length_line = [int(n) for n in conversion_line.split()]
    for to_convert_range_start, to_convert_range_length_number in number_ranges_to_convert.copy():
        if (source_range_start <= to_convert_range_start <= source_range_start + range_length_line and
                source_range_start <= to_convert_range_start + to_convert_range_length_number <= source_range_start + range_length_line
            ): 
            #   --------
            #     ----
            overlapping_range_start,overlapping_range_length = max(source_range_start, to_convert_range_start), min(source_range_start+range_length_line, to_convert_range_start + to_convert_range_length_number) - max(source_range_start, to_convert_range_start)
            new_number_ranges_to_convert += [( overlapping_range_start - (source_range_start - destination_range_start), overlapping_range_length)]
            converted_numbers += [(overlapping_range_start,overlapping_range_length)]

        elif (to_convert_range_start < source_range_start and to_convert_range_start+to_convert_range_length_number >= source_range_start):
            #      ----------
            # ---------
            overlapping_range_start,overlapping_range_length = max(source_range_start, to_convert_range_start), min(source_range_start+range_length_line, to_convert_range_start + to_convert_range_length_number) - max(source_range_start, to_convert_range_start)
            new_number_ranges_to_convert += [( overlapping_range_start - (source_range_start - destination_range_start), overlapping_range_length)]
            converted_numbers += [(overlapping_range_start,overlapping_range_length)]
            number_ranges_to_convert += [(to_convert_range_start, overlapping_range_start-to_convert_range_start)]



        elif (source_range_start <= to_convert_range_start <= source_range_start + range_length_line and to_convert_range_start+to_convert_range_length_number>source_range_start+range_length_line):
            #     -----------
            #          ----------
            overlapping_range_start,overlapping_range_length = max(source_range_start, to_convert_range_start), min(source_range_start+range_length_line, to_convert_range_start + to_convert_range_length_number) - max(source_range_start, to_convert_range_start)
            new_number_ranges_to_convert += [( overlapping_range_start - (source_range_start - destination_range_start), overlapping_range_length)]
            converted_numbers += [(overlapping_range_start,overlapping_range_length)]
            number_ranges_to_convert += [(overlapping_range_start+overlapping_range_length, 
                                          to_convert_range_start+to_convert_range_length_number - (source_range_start+range_length_line)
                                        )]
        else:
            number_ranges_to_convert += [(to_convert_range_start, to_convert_range_length_number)]
        number_ranges_to_convert.remove((to_convert_range_start, to_convert_range_length_number))


print(min(number_ranges_to_convert, key=lambda x: x[0])[0])