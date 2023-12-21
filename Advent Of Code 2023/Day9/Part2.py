f = open("./Advent Of Code 2023/Day9/input1.txt", "r").read().split("\n")
data = [line.split() for line in f]

def math(numberRow):
    array = []
    for i, number in enumerate(numberRow[:len(numberRow)-1]):
        array.append(int(numberRow[i + 1])- int(number))

    if array.count(0) != len(array):
        list(math(array))
    numberRow.insert(0 ,(int(numberRow[0]) -array[0]))
    return numberRow

result = 0
for record in data:
    result += math(record)[0]

print(result)