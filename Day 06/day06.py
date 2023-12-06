import math
with open("Day 06/input.txt") as file:
    lines = file.read().splitlines()

times = [int(time) for time in lines[0].split(":")[1].split()]
distances = [int(distance) for distance in lines[1].split(":")[1].split()]

#part two:
times = [int("".join([str(time) for time in times]))]
distances = [int("".join([str(distance) for distance in distances]))]



# math! 
# seconds_waited = x
# distance_travelled = (time - x)*x >  distance
#                     -x**2 +time*x  - distance > 0
#                       x**2 - time*x + distance < 0
#                     x = time +- (time**2 - 4*distance)**0.5 / 2


multiplication_of_ways_to_win = 1
for time, distance in zip(times, distances):
    maximum_wait_time_to_win = (time + ((-time)**2 - 4*distance)**0.5) / 2
    if maximum_wait_time_to_win == math.floor(maximum_wait_time_to_win):
        maximum_wait_time_to_win -=1
    else:
        maximum_wait_time_to_win =math.floor(maximum_wait_time_to_win)
    
    minimum_wait_time_to_win = (time - ((-time)**2 - 4*distance)**0.5) / 2
    if minimum_wait_time_to_win == math.ceil(minimum_wait_time_to_win):
        minimum_wait_time_to_win +=1 
    else:
        minimum_wait_time_to_win =math.ceil(minimum_wait_time_to_win)

    ways_to_win = maximum_wait_time_to_win-minimum_wait_time_to_win + 1
    multiplication_of_ways_to_win *= ways_to_win
print(multiplication_of_ways_to_win)

