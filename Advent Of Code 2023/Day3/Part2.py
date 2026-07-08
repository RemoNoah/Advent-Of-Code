from collections import defaultdict
import re
f = open("./Advent Of Code 2023/Day3/input1.txt", "r")

lines = f.read().splitlines()
adj = defaultdict(list)
for i, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        idxs = [(i, m.start() - 1), (i, m.end())]
        idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
        idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
        for a, b in idxs:
            if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != ".":
                adj[a, b].append(m.group())
print(sum(int(x[0]) * int(x[1]) for x in adj.values() if len(x) == 2))