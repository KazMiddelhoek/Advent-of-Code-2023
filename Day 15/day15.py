with open("Day 15/input.txt") as file:
    innitialization_sequence = file.read().splitlines()[0].split(",")

def HASH(string):
    current_value = 0
    for char in string:
        current_value+=ord(char)
        current_value*=17
        current_value%=256
    return  current_value

sum_of_hash_results = 0
for step in innitialization_sequence:
    current_value = HASH(step)
    sum_of_hash_results+=current_value
print(sum_of_hash_results)

# part two
boxes = {}
for step in innitialization_sequence:
    operation=step.find("=")
    if operation == -1:
        operation = step.find("-")
    label = step[:operation]
    box_number = HASH(label)
    if step[operation] == "-":
        boxes[box_number]=[elem for elem in boxes.get(box_number, []) if elem[0] != label]
    else:
        digit = int(step[operation+1:])
        label_in_box = [elem for elem in boxes.get(box_number, []) if elem[0] == label]
        if label_in_box:
            loc = boxes[box_number].index(label_in_box[0])
            boxes[box_number][loc][1] = digit
        else:
            boxes[box_number]=boxes.get(box_number, []) + [[label, digit]]

sum_of_focusing_powers = 0
for box, lenses in boxes.items():
    for slot_number, lens in enumerate(lenses,1):
        focusing_power = (1+box) * slot_number * lens[1]
        sum_of_focusing_powers += focusing_power
print(sum_of_focusing_powers)


