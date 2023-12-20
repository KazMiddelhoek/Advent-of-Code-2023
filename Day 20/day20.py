with open("Day 20/input.txt", newline="") as file:
    machine_list = file.read().splitlines()

BROADCASTER = "broadcaster"
machines = {"broadcaster": (BROADCASTER, machine_list[0].split(" -> ")[1].split(", "), "-")}
FLIP_FLOP = "%"
CONJUNCTION = "&"
OFF = 0
ON = 1
LOW = 0
HIGH = 1
for machine in machine_list[1:]:
    machine_name = machine.split(" -> ")[0][1:]
    machine_type = machine.split(" -> ")[0][0]
    machine_sends_to = machine.split(" -> ")[1].split(", ")

    machines[machine_name] = [machine_type, machine_sends_to]
    if machine_type == FLIP_FLOP:
        machines[machine_name] = machines[machine_name] + [OFF,]
    elif machine_type == CONJUNCTION:
        machines[machine_name] = machines[machine_name] + [{},]

for machine_name, (machine_type, machine_sends_to, state) in machines.items():
    for machine in machine_sends_to:
        if machine not in machines:
            continue
        if machines[machine][0] == CONJUNCTION:
            machines[machine][2][machine_name] = LOW

print(machines)
number_of_low_pulses_sent = 0
number_of_high_pulses_sent = 0

for _ in range(1000):
    number_of_low_pulses_sent +=1
    pulses_to_send = [("broadcaster", LOW, machines["broadcaster"][1])]
    while pulses_to_send:
        pulse_sent_by, sent_pulse, receivers = pulses_to_send.pop(0)
        for receiver in receivers:
            if sent_pulse == LOW:
                number_of_low_pulses_sent +=1
            elif sent_pulse == HIGH:
                number_of_high_pulses_sent +=1

            if receiver not in machines:
                continue
            if machines[receiver][0] == FLIP_FLOP and sent_pulse == LOW:
                machines[receiver][2] = int(not machines[receiver][2])
                if machines[receiver][2] == ON:
                    pulses_to_send.append((receiver, HIGH, machines[receiver][1]))
                else: 
                    pulses_to_send.append((receiver, LOW, machines[receiver][1]))
        
            if machines[receiver][0] == CONJUNCTION:
                machines[receiver][2][pulse_sent_by] = sent_pulse
                if all(machines[receiver][2].values()):
                    pulses_to_send.append((receiver, LOW, machines[receiver][1]))
                else:
                    pulses_to_send.append((receiver, HIGH, machines[receiver][1]))
                

print(number_of_low_pulses_sent)
print(number_of_high_pulses_sent)
print(number_of_low_pulses_sent*number_of_high_pulses_sent)

# part two

# a low pulse is sent to rx if high pulses are last sent to cl
# cl is dependent on js, qs, dt, ds
# so lets track when they send high pulses


BROADCASTER = "broadcaster"
machines = {"broadcaster": (BROADCASTER, machine_list[0].split(" -> ")[1].split(", "), "-")}
FLIP_FLOP = "%"
CONJUNCTION = "&"
OFF = 0
ON = 1
LOW = 0
HIGH = 1
for machine in machine_list[1:]:
    machine_name = machine.split(" -> ")[0][1:]
    machine_type = machine.split(" -> ")[0][0]
    machine_sends_to = machine.split(" -> ")[1].split(", ")

    machines[machine_name] = [machine_type, machine_sends_to]
    if machine_type == FLIP_FLOP:
        machines[machine_name] = machines[machine_name] + [OFF,]
    elif machine_type == CONJUNCTION:
        machines[machine_name] = machines[machine_name] + [{},]

for machine_name, (machine_type, machine_sends_to, state) in machines.items():
    for machine in machine_sends_to:
        if machine not in machines:
            continue
        if machines[machine][0] == CONJUNCTION:
            machines[machine][2][machine_name] = LOW

print(machines)
number_of_low_pulses_sent = 0
number_of_high_pulses_sent = 0
i = 0
high_pulse_required = {
    "js": [],
    "qs": [],
    "dt": [],
    "ts": [],
}
while not all(len(high_pulse_sent_moment) == 2 for high_pulse_sent_moment in high_pulse_required.values()):
    i+=1
    pulses_to_send = [("broadcaster", LOW, machines["broadcaster"][1])]
    while pulses_to_send:
        pulse_sent_by, sent_pulse, receivers = pulses_to_send.pop(0)
        if sent_pulse == HIGH and pulse_sent_by in high_pulse_required:
            high_pulse_required[pulse_sent_by].append(i)
        for receiver in receivers:
            if receiver not in machines:
                continue
            if machines[receiver][0] == FLIP_FLOP and sent_pulse == LOW:
                machines[receiver][2] = int(not machines[receiver][2])
                if machines[receiver][2] == ON:
                    pulses_to_send.append((receiver, HIGH, machines[receiver][1]))
                else: 
                    pulses_to_send.append((receiver, LOW, machines[receiver][1]))
        
            if machines[receiver][0] == CONJUNCTION:
                machines[receiver][2][pulse_sent_by] = sent_pulse
                if all(machines[receiver][2].values()):
                    pulses_to_send.append((receiver, LOW, machines[receiver][1]))
                else:
                    pulses_to_send.append((receiver, HIGH, machines[receiver][1]))
print(high_pulse_required)

from functools import reduce
from math import gcd
def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)
cycles = [end-start for (start,end) in  high_pulse_required.values()]
print(lcm(cycles))