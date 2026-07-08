f = open("./Advent Of Code 2023/Day4/input1.txt", "r")
inputs = f.read().split("\n")

count = []
cardCount = 0

for index,input in enumerate(inputs):
    count.append([index + 1, 1])

for record in count:
    recordIndex = record[0] -1
    recordCount = record[1]
    winningNumbers = inputs[recordIndex].split("|")[0].split(":")[1].split(" ")
    myNumbers = inputs[recordIndex].split("|")[1].split(" ")
    points = 0
    
    for myNumber in myNumbers:
        if myNumber != '':
            for winningNumber in winningNumbers:
                if winningNumber != '':
                    if winningNumber == myNumber:
                        points += 1
    
    for index in range(0, points):
        if len(count) > index + 1:
            count[index + recordIndex + 1][1] += recordCount

for record in count:
    cardCount += record[1]
print(cardCount)