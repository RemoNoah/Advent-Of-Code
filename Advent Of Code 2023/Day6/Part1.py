times, distances = [line.split()[1:] for line in open("./Advent Of Code 2023/Day6/input1.txt", "r").read().split("\n")]
for time in times:
    i = time

f = open("./Advent Of Code 2023/Day6/input1.txt", "r").read().split("\n")

def p1(f):
    races = [map(int, line.split()[1:]) for line in f]
    ans = 1
    for time, dist in zip(*races):
        ans *= sum((time - hold) * hold >= dist for hold in range(time))
    return ans

print(p1(f))

import math
def p2(f):
    time, dist = [int(line.replace(" ", "").split(":")[1]) for line in f]
    a = (time - math.sqrt(time**2 - 4 * dist)) / 2
    b = (time + math.sqrt(time**2 - 4 * dist)) / 2
    return math.floor(b) - math.ceil(a) + 1

print(p2(f))      