lines = open("./Advent Of Code 2023/Day10/input.txt", "r").read().splitlines()

#[step, digit, x, y]
coordinates = []

def pattern(currentCoordinates, coordinatesBefor):
    
    #[x, y]
    next = [currentCoordinates[2],currentCoordinates[3]]   
    if currentCoordinates[1] == "-":
        if next[0] > coordinatesBefor[2]:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]][next[0]+1],next[0] +1, next[1]])
        else:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]][next[0]-1],next[0] -1, next[1]])
            
    elif currentCoordinates[1] == "|":
        if next[1] < coordinatesBefor[3]:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]-1][next[0]],next[0], next[1]-1])
        else:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]+1][next[0]],next[0], next[1]+1])
            
    elif currentCoordinates[1] == "L":
        if next[1] > coordinatesBefor[3]:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]][next[0]+1],next[0] +1, next[1]])
        else:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]-1][next[0]],next[0], next[1]-1])
            
    elif currentCoordinates[1] == "J":
        if next[1] > coordinatesBefor[3]:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]][next[0]-1],next[0] -1, next[1]])
        else:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]-1][next[0]],next[0], next[1]- 1])
            
    elif currentCoordinates[1] == "7":
        if next[1] < coordinatesBefor[3]:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]][next[0]-1],next[0] -1, next[1]])
        else:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]+1][next[0]],next[0], next[1] + 1])
            
    elif currentCoordinates[1] == "F":
        if next[1] < coordinatesBefor[3]:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]][next[0]+1],next[0] +1, next[1]])
        else:
            coordinates.append([currentCoordinates[0] +1, lines[next[1]+1][next[0]],next[0], next[1] + 1])
            
    return        
            
for y, line in enumerate(lines):
    if "S" in line:
        coordinates.append([0, "S",line.index("S"), y])
        coordinates.append([1, "L",line.index("S"), y+ 1])
        break
    
while coordinates[-1][1] != "S":
    pattern(coordinates[-1], coordinates[-2])
    
print((len(coordinates)-1)/2)
