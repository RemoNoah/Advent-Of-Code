f = open("./day1/input.txt", "r").read().splitlines()

counter = 50
p1 = 0
p2 = 0

for line in f:
    d = line[0]
    n = int(line[1:])

    for i in range(n):
        if d == 'L':
            counter = (counter-1+100)%100
        else:
            counter = (counter+1)%100
        if counter == 0:
            p2 += 1
    if counter == 0:
        p1 += 1

print(p1, p2)


