with open("Day 09/input.txt") as file:
    histories = [[int(measurement) for measurement in history.split()] for history in file.read().splitlines()]

sum_of_extrapolated_values = 0
for history in histories:
    last_values_of_sequence = [history[-1]]
    diffs = [next_measurement-measurement for measurement, next_measurement in zip(history[:-1], history[1:])]
    while not all(diff == 0 for diff in diffs):
        last_values_of_sequence.append(diffs[-1])
        diffs = [next_measurement-measurement for measurement, next_measurement in zip(diffs[:-1], diffs[1:])]

    extrapolated_value = sum(last_values_of_sequence)
    sum_of_extrapolated_values += extrapolated_value
print(sum_of_extrapolated_values)
 
# part two
sum_of_extrapolated_previous_values = 0
for history in histories:
    first_values_of_sequence = [history[0]]
    diffs = [next_measurement-measurement for measurement, next_measurement in zip(history[:-1], history[1:])]
    while not all(diff == 0 for diff in diffs):
        first_values_of_sequence.append(diffs[0])
        diffs = [next_measurement-measurement for measurement, next_measurement in zip(diffs[:-1], diffs[1:])]

    extrapolated_first_value = sum(first_values_of_sequence[::2]) - sum(first_values_of_sequence[1::2])
    sum_of_extrapolated_previous_values += extrapolated_first_value
print(sum_of_extrapolated_previous_values)


