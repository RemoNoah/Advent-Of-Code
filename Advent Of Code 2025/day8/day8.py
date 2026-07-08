data = open("./day8/input.txt", "r").read().splitlines()

def data_setup(data):
    cleaned_data = []
    for line in data:
        cleaned_data.append([int(x) for x in line.split(",")])
    return cleaned_data

def calculate_distance(point1, point2):
    vektor = (point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2])
    distance = (vektor[0]**2 + vektor[1]**2 + vektor[2]**2) ** 0.5
    return distance

def get_all_distances(all_junction_boxes_positions):
    all_distances = []
    for i in range(len(all_junction_boxes_positions)):
        for j in range(i + 1, len(all_junction_boxes_positions)):
            distance = calculate_distance( all_junction_boxes_positions[i], all_junction_boxes_positions[j] )
            all_distances.append([i, j, distance])
    return all_distances

def get_all_cercuits(data, sorted_distances, connetction_count):
    cercuits = []
    cercuits_contains = set()
    cercuits_has_all = False
    for i in range(connetction_count):

        in_cercuit = False
        in_cercuit_indexes = []
        for index, cercuit in enumerate(cercuits):
            if sorted_distances[i][0] in cercuit or sorted_distances[i][1] in cercuit:
                cercuit.add(sorted_distances[i][0])
                cercuit.add(sorted_distances[i][1])
                cercuits_contains.add(sorted_distances[i][0])
                cercuits_contains.add(sorted_distances[i][1])
                in_cercuit_indexes.append(index)
                in_cercuit = True
                

        if len(in_cercuit_indexes) > 1:
            first_cercuit_index = in_cercuit_indexes[0]
            for j in range(1, len(in_cercuit_indexes)):
                cercuits[first_cercuit_index] = cercuits[first_cercuit_index].union(cercuits[in_cercuit_indexes[j]])

            # Remove merged cercuits (iterate backwards to avoid index shifting)
            for j in range(len(in_cercuit_indexes)-1, 0, -1):
                del cercuits[in_cercuit_indexes[j]]

        if not in_cercuit:
            cercuits.append(set([sorted_distances[i][0], sorted_distances[i][1]]))
            cercuits_contains.add(sorted_distances[i][0])
            cercuits_contains.add(sorted_distances[i][1])

        if cercuits_contains == set(range(len(data))):
            cercuits_has_all = True

        # part2
        if len(cercuits) == 1 and cercuits_has_all:
            return data[sorted_distances[i][0]][0]*data[sorted_distances[i][1]][0] 
    return cercuits
    

def part1(data):
    cleaned_data = data_setup(data)
    all_distances = get_all_distances(cleaned_data)
    sorted_distances = sorted(all_distances, key=lambda x: x[2])

    how_many_connections = 1000
    all_cercuits = get_all_cercuits(cleaned_data, sorted_distances, how_many_connections)
    sorted_cercuits = sorted(all_cercuits, key=lambda x: len(x), reverse=True)

    multipli_cercuits_count = 3
    p1 = len(sorted_cercuits[0])
    for i in range(multipli_cercuits_count - 1):
        p1 *= len(sorted_cercuits[i + 1])

    print(p1)

def part2(data):
    cleaned_data = data_setup(data)
    all_distances = get_all_distances(cleaned_data)
    sorted_distances = sorted(all_distances, key=lambda x: x[2])

    how_many_connections = 100000
    p2 = get_all_cercuits(cleaned_data, sorted_distances, how_many_connections)
    print(p2)

part1(data.copy())
part2(data.copy())