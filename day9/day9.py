data = open("./day9/input.txt", "r").read().splitlines()

def data_setup(data):
    cleaned_data = []
    for line in data:
        cleaned_data.append([int(x) for x in line.split(",")])
    return cleaned_data

def get_area(p1, p2):
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height

def part1(data):
    cleaned_data = data_setup(data)
    max_area = 0
    
    for i in range(len(cleaned_data)):
        for j in range(i + 1, len(cleaned_data)):
            current_area = get_area(cleaned_data[i], cleaned_data[j])
            
            if current_area > max_area:
                max_area = current_area
                
    print("Part 1:", max_area)

part1(data)