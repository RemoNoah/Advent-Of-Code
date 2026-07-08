f = open("./day3/input.txt", "r").read().splitlines()

p1 = 0

for line in f:
    firstNumber = 0
    secondNumber = 0
    for i, d in enumerate(line):
        d = int(d)
        ifset = False
        if i +1 < len(line):
            if d > firstNumber:
                firstNumber = d
                secondNumber = 0
                ifset = True
        if d > secondNumber and not ifset:
            secondNumber = d
        
    
    p1 += int(str(firstNumber) + str(secondNumber))



p2 = 0
digits = [0,1,1,1,1,1,1,1,1,1,1,1]

def checkdigits(indexLine, d, lineLength, want=0):
    
    if want > 11:
        return
    
    if indexLine + (12-want) > lineLength:
        checkdigits(indexLine, d, lineLength, want+1)
        return
    
    if d > digits[want]:
        digits[want] = d
        for i in range(want+1, len(digits[want:])):
            digits[i] = 0
            
        return
    
    checkdigits(indexLine, d, lineLength, want+1)

    
        


for line in f:
    digits = [0,1,1,1,1,1,1,1,1,1,1,1]
    for i, d in enumerate(line):
        d = int(d)
        checkdigits(i, d, len(line))
    print(int("".join(map(str, digits))))
    p2 += int("".join(map(str, digits)))
     
     
print(p1)   
print(p2)
    


