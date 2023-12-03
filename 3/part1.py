from dataclasses import dataclass


@dataclass
class Part:
    string_num: list[str]
    pos: list[tuple[int, int]]


current_engine = Part([], [])

parts = []
symbols = set()

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c.isdigit():
                current_engine.string_num.append(c)
                current_engine.pos.append((row, col))
            else:
                if len(current_engine.string_num) > 0:
                    parts.append(current_engine)
                    current_engine = Part([], [])

                if c != '.':
                    symbols.add((row, col))
        if len(current_engine.string_num) > 0:
            parts.append(current_engine)
        current_engine = Part([], [])
    if len(current_engine.string_num) > 0:
        parts.append(current_engine)


real_parts = []
for part in parts:
    part_added = False
    for pos in part.pos:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                neighbor = (pos[0] + dx, pos[1] + dy)
                if neighbor in symbols:
                    if not part_added:
                        real_parts.append(int(''.join(part.string_num)))
                        part_added = True
print(parts)
print(real_parts)
print(sum(real_parts))