instructions , *f = open("./Advent Of Code 2023/Day8/input1.txt", "r").read().split("\n")
data = []
currentMaps = []

for maping in [a.split() for a in f[1:]]:
    data.append([ i.replace('(', '').replace(')', '').replace(',', '') for i in  maping])
    if 'A' in maping[0][2]:
        currentMaps.append(maping[0])
        
test = []
for index, current in enumerate(currentMaps):
    steps = 0
    isSearch = True
    while isSearch:
        for instruction in instructions:
                for i, map in enumerate(data):
                    if current in map[0]:
                        if instruction == 'R':
                            current = map[3]
                        else:
                            current = map[2]
                        steps += 1
                        break
                if current[-1] == 'Z':
                    isSearch = False
                    print(steps)
                    break
    test.append([index, steps])
    
result = 1      
for int in test:
     result *= int[1]
    
print(result)




#for each map in current
#1 time all imstructions
#list of the result

#KGV of all