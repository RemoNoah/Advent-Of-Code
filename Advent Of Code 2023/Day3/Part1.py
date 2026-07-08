import re
f = open("./Advent Of Code 2023/Day3/input1.txt", "r")

lines = f.read().splitlines()
ans = 0
for i, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        idxs = [(i, m.start() - 1), (i, m.end())]
        idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
        idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
        count = sum(0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != "." for a, b in idxs)
        if count > 0:
            ans += int(m.group())
print(ans)