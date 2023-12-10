from typing import Callable, Tuple
import re


def mapt(function: Callable, *sequences) -> tuple:
    return tuple(map(function, *sequences))
def ints(text: str) -> Tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'-?[0-9]+', text))


I = open('./input.txt').read().splitlines()
n = mapt(ints, I)
races = list(zip(*n))
races = [ (51699878, 377117112241505)]

wins = []
for t, r in races:
    s = 0
    w = 0
    for p in range(t):
        l = (t-p)*s
        if l > r:
            w += 1
        s += 1
    wins.append(w)
print(wins)

