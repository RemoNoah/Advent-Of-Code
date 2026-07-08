import math
lines = open("./Advent Of Code 2023/Day11/input.txt", "r").read().splitlines()

dubbleRowIndex = []
dubbleColumnsIndex = []

galaxies = []

for iL, line in enumerate(lines):
        if "#" not in line:
            dubbleRowIndex.append(iL)

for iC in range(len(lines[0])):
    isIn = False
    for iL in range(len(lines)):
        if "#" == lines[iL][iC]:
            isIn = True
            countL = sum(list(map(lambda num:num < iL, dubbleRowIndex))) * 999999
            countC = sum(list(map(lambda num:num < iC, dubbleColumnsIndex))) * 999999
            galaxies.append([iL+countL,iC+countC])
    if isIn != True:
        dubbleColumnsIndex.append(iC)

result = 0
for i, galaxy in enumerate(galaxies):
    for x in range(i+1, len(galaxies)):
        steps = math.dist([galaxies[x][0]], [galaxy[0]]) + math.dist([galaxies[x][1]], [galaxy[1]])
        result += steps
        
print(result)