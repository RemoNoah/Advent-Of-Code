import os

f = open("./Advent Of Code 2023/Day1/input1.txt", "r")
inputs = f.read().split("\n")

def get(inputs):
    
    results = 0
    for input in inputs:
        result = ""
        
        for element in input:
            if element.isnumeric() and element.isdecimal():
                result += element
                break
            
        if len(result) > 0:
            lenght = len(input)
            while lenght > 0:
                element = input[lenght -1]
                if element.isnumeric() and element.isdecimal() :
                    result += element
                    break
                lenght -= 1
            
            results +=int(result)
        
    return results

print(get(inputs))