f = open("./day2/input.txt", "r").read().split(",")
data = [line for line in f if line]

p1 = 0
p2 = 0

def getInvalid(n, length=1):
    global p2
    s = str(n)
    if len(s) <= length:
        return
    
    if len(s) % length != 0:
        getInvalid(n, length+1)
        return
    
    digits = [] 

    for i in range(0, len(s), length):
        digits.append(s[i:i+length])

    count = 0
    for d in digits:
        if d == digits[0]:
            count += 1
    
    if count == len(digits):
        p2 += n
        return
    
    getInvalid(n, length+1)

for line in data:
    start, end = line.split("-")

    for i in range(int(start), int(end)+1):
        if i > 10:
            first, second =  str(i)[:len(str(i))//2], str(i)[len(str(i))//2:]
            if first == second:
                p1 += i
        getInvalid(i)

print(p1, p2)