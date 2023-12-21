instructions , *f = open("./Advent Of Code 2023/Day8/input1.txt", "r").read().split("\n")

maps = [a.split() for a in f[1:]]
data = []
currentMaps = []
steps = 0
isSearch = True

for maping in maps:
    data.append([ i.replace('(', '').replace(')', '').replace(',', '') for i in  maping])
    if 'A' in maping[0][2]:
        currentMaps.append(maping[0])

while isSearch:
    for instruction in instructions:
        
        for index, current in enumerate(currentMaps):
            
            for i, maping in enumerate(data):
                
                if current in maping[0]:
                    if instruction == 'R':
                        currentMaps[index] = maping[3]
                    else:
                        currentMaps[index] = maping[2]
                    break
        steps += 1
        
        if sum(x[2].count('Z') for x in currentMaps) == len(currentMaps):
            print(steps)
            isSearch = False
            break
    
print("a")