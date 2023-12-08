with open("Day 08/input.txt") as file:
    lines = file.read().splitlines()

instructions = lines[0]
nodes = {node.split(" = ")[0]: node.split(" = ")[1][1:-1].split(", ")  for node in lines[2:]}

current_position = "AAA"
steps_taken = 0
while current_position != "ZZZ":
    direction_to_take = instructions[steps_taken % (len(instructions))]
    current_position = nodes[current_position][0 if direction_to_take =="L" else 1]
    steps_taken +=1
print(steps_taken)

# part two
import math
from functools import reduce

current_positions = [node for node in nodes if node.endswith("A")]

steps_needed_per_position = []
for current_position in current_positions:
    steps_taken = 0
    while not current_position.endswith("Z"):
        direction_to_take = instructions[steps_taken % (len(instructions))]
        current_position = nodes[current_position][0 if direction_to_take =="L" else 1] 
        steps_taken +=1
    steps_needed_per_position.append(steps_taken)

def lcm(arr):
    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

print(lcm(steps_needed_per_position))



