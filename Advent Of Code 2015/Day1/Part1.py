f = open("./Advent Of Code 2015/Day1/input1.txt", "r")
inputs = f.read()

floorlevel = 0
for char in inputs:
    if char == '(':
        floorlevel += 1
    else:
        floorlevel -= 1

print(floorlevel)