import itertools
import math
import re

input = open('input.txt').read().splitlines()
moves = itertools.cycle(list(input[0]))
waypoints = input[2:]
waypoints = [re.findall(r'[\w]+', w) for w in waypoints]

def parse(waypoints):
    for n, l, r in waypoints:
        yield 'L' + n, l
        yield 'R' + n, r

waypoints = dict(parse(waypoints))
starting_waypoints = []
for k in waypoints.keys():
    if k[-1] == 'A':
        starting_waypoints.append(k[1:])

print(starting_waypoints)


all_cycles = []

for w in starting_waypoints:
    found = False
    current = w
    cycles = 0
    while not found:
        ins = next(moves)
        key = ins + current
        value = waypoints[key]

        if value[-1] == 'Z':
            found = True
        current = value
        cycles += 1
    all_cycles.append(cycles)
    moves = itertools.cycle(list(input[0]))

print(all_cycles)

print(math.lcm(*all_cycles))