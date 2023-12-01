import os
f = open("./Advent Of Code 2023/Day1/input2.txt", "r")
inputs = f.read().split("\n")

spelled = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_indexes(string ,word,indexes = [], start = 0, ):
    index = string.find(word, start)
    if index >= 0:
        indexes.append(index)
        get_indexes(string, word,indexes, index + 1)
    return indexes

def get_indeesOfDigitList(string, digits):
    indexesOfDigits = []
    for digit in digits:
        indexesOfDigit = get_indexes(string, digit, [])
        for indexOfDigit in indexesOfDigit:
            indexesOfDigits.append([indexOfDigit, digit])
    return indexesOfDigits

def get_number(digits, spelledDigets):
    numbers = ""
    for digit in digits:
        if digit.isnumeric():
            numbers += digit
        else:
            numbers += str(spelledDigets.index(digit))
            
    return int(numbers)

def main(inputs):
    results = 0
    for input in inputs:
        indexesOfSpelledDigets = []
        
        spelledDigits = [substring for substring in spelled if substring in input]    
        digits = [substring for substring in numbers if substring in input]    
        
        indexesOfSpelledDigets += get_indeesOfDigitList(input, spelledDigits)
        indexesOfSpelledDigets += get_indeesOfDigitList(input, digits)

        sorted_list = sorted(indexesOfSpelledDigets, key=lambda x: x[0])
        if len(sorted_list) > 0:
            selectedSorted_list = sorted_list[0][1] , sorted_list[len(sorted_list) -1][1]
            results += get_number(selectedSorted_list, spelled)
    return results


    
print(main(inputs))
