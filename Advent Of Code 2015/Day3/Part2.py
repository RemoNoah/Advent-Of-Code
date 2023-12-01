f = open("./Advent Of Code 2015/Day3/input1.txt", "r")
input = f.read()

isSanta = True
currentVectSanta = [0,0]
currentVectRobot = [0,0]
listOfVect = [[0,0]]

def main(vect, move):
    if move == '<':
        newVect = [vect[0] - 1, vect[1]]
    elif move == '>':
        newVect = [vect[0] + 1, vect[1]]
    elif move == '^':
        newVect = [vect[0],vect[1] +1]
    elif move == 'v':
        newVect = [vect[0],vect[1] -1]
        
    if newVect not in listOfVect:
        listOfVect.append(newVect)

    return newVect


for move in input:
    if(isSanta):
        currentVectSanta = main(currentVectSanta, move)
        isSanta = not isSanta
    else:
        currentVectRobot = main(currentVectRobot, move)
        isSanta = not isSanta
    
print(len(listOfVect))