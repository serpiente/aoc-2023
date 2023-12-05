import re
from collections import defaultdict
from copy import copy

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    wins = defaultdict(int)

    copies = defaultdict(int)

    for line in lines:
        gameid, numbers = line.split(':')
        gameid = int(re.findall("\d+", gameid)[0])
        hand, winning = numbers.split('|')
        hand = set([h for h in hand.split(' ') if h != ''])
        winning = set([w for w in winning.split(' ') if w != ''])

        score = None
        for number in hand:
            if number in winning:
                wins[gameid] += 1
            copies[gameid] = 1

    for wining_id, num in wins.items():
        for _ in range(copies[wining_id]):
            for i in range(1, num + 1):
                game_id = wining_id + i
                copies[game_id] += 1

    print(sum(copies.values()))


