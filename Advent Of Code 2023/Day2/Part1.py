f = open("./Advent Of Code 2023/Day2/input1.txt", "r").read().splitlines()

for line in f:
    gameId, shown = line.split(": ")
    gameId = int(gameId.split(" ")[1])
    shown = map(str.split, shown.split("; "))
    print(list(shown))