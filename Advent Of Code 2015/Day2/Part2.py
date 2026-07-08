import math
f = open("./Advent Of Code 2015/Day2/input1.txt", "r")
inputs = f.read().split("\n")

total = 0

for input in inputs:
    dimensions = input.split("x")
    i = len(dimensions)
    while i > 0:
        dimensions[i-1] = int(dimensions[i-1])
        i -= 1
        
    dimensions.sort()
    
    ribbonNeeded = 2*(dimensions[0]+dimensions[1])
    ribbonBow = dimensions[0]*dimensions[1]*dimensions[2]

    total += ribbonNeeded + ribbonBow

print(total)
