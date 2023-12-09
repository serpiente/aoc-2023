from collections import Counter
from dataclasses import dataclass
from functools import total_ordering


ranks = 'J23456789TQKA'


def handrank(hand):
    hand_rnks = list(map(ranks.index , hand))
    counts = Counter(hand_rnks)
    j = counts[0]
    del counts[0]
    groups = sorted(((counts[r]) for r in counts), reverse=True)
    if groups: #meh, hack to go around JJJJJ
        groups[0] = groups[0] + j
    else:
        groups = [5]
    return tuple(groups + hand_rnks)

lines = open('./input.txt').read().splitlines()
hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

sorted_hands = sorted(hands, key=lambda x: handrank(x[0]))

ans1 = sum([(i+1)*w for i, (_, w) in enumerate(sorted_hands)])

print(ans1)
