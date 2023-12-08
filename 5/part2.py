def parse(I, i=3):
    while i < len(I):
        mapping = []
        while i < len(I) and I[i] != '':
            to, fr, rng = (int(n) for n in I[i].split())
            mapping.append([fr, fr + rng, to - fr])
            i += 1
        yield sorted(mapping)
        i += 2


def translate(maps, ranges):
    for s, e in ranges:
        for fr, to, o in maps:
            yield s, min(e, fr)
            yield max(s, fr) + o, min(e, to) + o
            s = max(s, min(to, e))
        yield s, e


def solve(mappings, seeds):
    for mapping in mappings:
        seeds = [(a, b) for a, b in translate(mapping, seeds) if a < b]
    return min(a for a, b in seeds)


txt = open('./input.txt').read().splitlines()
seeds = [int(x) for x in txt[0].split(':')[1].split()]
mappings = list(parse(txt))
answer2 = solve(mappings, ((x, x+y) for x, y in zip(seeds[::2], seeds[1::2])))
print(answer2)