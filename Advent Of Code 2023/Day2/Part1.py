f = open("./Advent Of Code 2023/Day2/input1.txt", "r")
inputs = f.read().split("\n")

checkRed = 12
checkGreen = 13
checkBlue = 14
gameSum = 0

for record in inputs:
    gameId = int(record.split(":")[0].split(" ")[1])
    
    show = record.split(":")[1].split(";")
    statusGame = 0
    
    for example in show:
        data = example.split(",")
        
        statusexample = 0
        
        for cubes in data:
            value = int(cubes.split(" ")[1])
            color = cubes.split(" ")[2]
            
            if color == "green" and value < checkGreen:
                statusexample += 1
            elif color == "red" and value < checkRed:
                statusexample += 1
            elif color == "blue" and value < checkBlue:
                statusexample += 1
                
        if statusexample == len(data):
            statusGame += 1
            
    if statusGame == len(show):
        gameSum += gameId
        
print(gameSum)