f = open("./Advent Of Code 2023/Day9/input1.txt", "r").read().split("\n")
data = [line.split() for line in f]

def math(numberRow):
    array = []
    for i, number in enumerate(numberRow[:len(numberRow)-1]):
        array.append(int(numberRow[i + 1])- int(number))
    
    #array = list(map(lambda num: int(numberRow[numberRow.index(num)+1]) - int(num) , numberRow[:len(numberRow) -1]))

    if array.count(0) != len(array):
        list(math(array))
    numberRow.append(array[-1] + int(numberRow[-1]))
    return numberRow

result = 0
for record in data:
    result += math(record)[-1]

print(result)