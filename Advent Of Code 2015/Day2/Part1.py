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
        
    paperNeeded = 2*(int(dimensions[0])*int(dimensions[1]) + int(dimensions[1])*int(dimensions[2]) + int(dimensions[0])*int(dimensions[2]))
    dimensions.sort()
    extrapaper = int(dimensions[0])*int(dimensions[1])
    total += paperNeeded + extrapaper

print(total)
