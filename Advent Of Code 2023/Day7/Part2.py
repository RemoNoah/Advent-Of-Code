f = open("./Advent Of Code 2023/Day7/input1.txt", "r").read().split("\n")
map = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def sortPlaysInType(play):
    result = []
    for char in play[0]:
        result.append(map.index(char))
    return result

def classify(hand):
    add = 0
    if "J" in hand:
        add = hand.count("J")

    counts = [hand.count(card) + add for card in hand.replace('J', '')]

    if 5 in counts or "JJJJJ" == hand:
        return 6
    elif 4 in counts:
        return 5
    elif 3 in counts:
        if add != 0:
            if counts.count(3) == 4 and add == 1:
                return 4
            for i, x in enumerate(counts):
                if x != 3:
                    counts[i] = x - add
        if 2 in counts:
            return 4
        return 3
    elif counts.count(2) == 4 and len(counts) == 5:
        return 2
    elif 2 in counts:
        return 1
    return 0

types = [[],[],[],[],[],[],[]]

for line in f:
    hand, bid = line.split()
    classHand = classify(hand)
    types[classHand].append((hand, int(bid)))

final = []
for type in types:
    type.sort(key=lambda x: sortPlaysInType(x))
    for hand in type:
        final.append(hand)

total = 0

for rank, card in enumerate(final):
    total += (rank + 1) * card[1]

print(total)