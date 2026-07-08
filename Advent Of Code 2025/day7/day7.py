import os
clear = lambda: os.system('cls')

data = open("./day7/input.txt", "r").read().splitlines()

def create_collision_sets(data):
    list_of_collision_sets = []
    
    for line in data:
        collision_set = set()
        for charIndex, char in enumerate(line):
            if char == "^":
                collision_set.add((charIndex))
        list_of_collision_sets.append(collision_set)

    return list_of_collision_sets

def get_starter_set(data):
    starter_set = set()
    for charIndex, char in enumerate(data[0]):
        if char == "S":
            starter_set.add((charIndex))
    return starter_set


def update_visual_data(visual_data, current_set, lineIndex):
    new_line = ""
    for charIndex, char in enumerate(visual_data[lineIndex]):
        if charIndex in current_set:
            new_line += "|"
        else:
            new_line += char
    visual_data[lineIndex] = new_line

    return visual_data

def print_visual_data(visual_data):
    clear()
    for line in visual_data:
        print(line)


def part_one(data):
    p1 = 0
    visual_data = data.copy()
    collision_sets = create_collision_sets(data)
    starter_set = get_starter_set(data)

    for lineIndex, collision_set in enumerate(collision_sets):
        # Get all intersections of the starter set and collision set
        intersection = starter_set.intersection(collision_set)
        p1 += len(intersection)

        # Create next starter set by removing collisions and adding all possible moves
        next_starter_set = starter_set.difference(collision_set)
        for position in intersection:
            # Move left
            next_starter_set.add(position - 1)

            # Move right
            next_starter_set.add(position + 1)
        
        starter_set = next_starter_set
    
        visual_data = update_visual_data(visual_data, starter_set, lineIndex)
        print_visual_data(visual_data)

    return p1


print("Part 1:", part_one(data))


def part_two(data):
    current_paths = {}
    
    for charIndex, char in enumerate(data[0]):
        if char == "S":
            current_paths[charIndex] = 1
    
    for line in data:
        next_paths = {}
        
        for position, count in current_paths.items():
            char = line[position]
            
            if char == "^":
                # Move Left
                next_paths[position - 1] = next_paths.get(position - 1, 0) + count
                # Move Right:
                next_paths[position + 1] = next_paths.get(position + 1, 0) + count
            
            else:
                next_paths[position] = next_paths.get(position, 0) + count
        
        current_paths = next_paths

    return sum(current_paths.values())

print("Part 2:", part_two(data))