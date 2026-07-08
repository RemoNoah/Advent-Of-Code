instructions , *f = open("./Advent Of Code 2023/Day8/input1.txt", "r").read().split("\n")

maps = [a.split() for a in f[1:]]
data = []
for map in maps:
    data.append([ i.replace('(', '').replace(')', '').replace(',', '') for i in  map])

current = 'AAA'
steps = 0
isSearch = True

while isSearch:
    for instruction in instructions:
        for i, map in enumerate(data):
            if current in map[0]:
                if instruction == 'R':
                    current = map[3]
                else:
                    current = map[2]
                steps += 1
                break
        if current == "ZZZ":
            isSearch = False
            print(steps)
            break