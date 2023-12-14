f = open("./Advent Of Code 2023/Day7/input1.txt", "r").read().split("\n")
map = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def classify(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    elif 4 in counts:
        return 5
    elif 3 in counts:
        if 2 in counts:
            return 4
        return 3
    elif counts.count(2) == 4:
        return 2
    elif 2 in counts:
        return 1
    return 0

types = [[],[],[],[],[],[],[]]

for line in f:
    hand, bid = line.split()
    classHand = classify(hand)
    types[classHand].append((hand, int(bid)))

def s(play):
    result = []
    for char in play[0]:
        result.append(map.index(char))
    return result

final = []
for type in types:
    type.sort(key=lambda x: s(x))
    for hand in type:
        final.append(hand)

total = 0

for rank, card in enumerate(final):
    total += (rank + 1) * card[1]

print(total)