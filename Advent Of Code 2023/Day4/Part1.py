f = open("./Advent Of Code 2023/Day4/input1.txt", "r")
inputs = f.read().split("\n")

ans = 0
for record in inputs:
    winningNumbers = record.split("|")[0].split(":")[1].split(" ")
    myNumbers = record.split("|")[1].split(" ")
    result = 0
    
    for myNumber in myNumbers:
        if myNumber != '':
            for wnumber in winningNumbers:
                if wnumber != '':
                    if wnumber == myNumber:
                        if result == 0:
                            result = 1
                        else:
                            result *= 2
    ans += result

print(ans)