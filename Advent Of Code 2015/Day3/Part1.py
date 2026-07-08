f = open("./Advent Of Code 2015/Day3/input1.txt", "r")
input = f.read()

currentVect = [0,0]
listOfVect = [[0,0]]

for move in input:
    if move == '<':
        newVect = [currentVect[0] - 1, currentVect[1]]
    elif move == '>':
        newVect = [currentVect[0] + 1, currentVect[1]]
    elif move == '^':
        newVect = [currentVect[0],currentVect[1] +1]
    elif move == 'v':
        newVect = [currentVect[0],currentVect[1] -1]
        
    if newVect in listOfVect:
        newIndex = listOfVect.index(newVect)
    else:
        listOfVect.append(newVect)
    currentVect = newVect
        
print(len(listOfVect))