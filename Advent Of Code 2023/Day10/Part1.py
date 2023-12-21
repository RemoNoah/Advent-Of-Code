lines = open("./Advent Of Code 2023/Day10/input.txt", "r").read().splitlines()

#[step, x, y]
coordinates = []

def getPath(currentCoordinates,lines):
    currentDigits = lines[currentCoordinates[1]][currentCoordinates[2]]
    
    print(currentDigits)

for y, line in enumerate(lines):
    if "S" in line:
        coordinates.append([0, line.index("S"), y])
        break

getPath(coordinates[0], lines)
    
print(coordinates)