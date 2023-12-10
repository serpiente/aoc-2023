import itertools
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

found = False
current = 'AAA'
cycles = 0
while not found:
    ins = next(moves)
    key = ins + current
    value = waypoints[key]

    if 'ZZZ' in value:
        found = True
    current = value
    cycles += 1
print(cycles)