f = open("./Advent Of Code 2023/Day5/input1.txt", "r").read().split("\n\n")

def mapData(var):
    return list(map(str.split , var.split("\n")[1:]))

def mapTo(search, maps):
    result = search
    for map in maps:
        if search in range(int(map[1]), int(map[1]) + int(map[2])):
            result = search + int(map[0]) - (int(map[1]))
            break
    return result

f[0] = seeds = [int(s) for s in f[0].split(" ")[1:]]
for i, var in enumerate(f[1:]):
    f[i + 1] = mapData(var)

finalLocation = -1
location  = ""
for seed in seeds:
    for i,maps in enumerate(f[1:]):
        if i == 0:
            location = mapTo(seed, maps)
        else:
            location = mapTo(location, maps)
    if finalLocation < 0 or finalLocation > location:
        finalLocation = location
        
print(finalLocation)