data = open("./day4/input.txt", "r").read().splitlines()

integral_image = []
binary_index = []
p1_grid_size = 3
p1 = 0

def get_binary(char):
    if char == "@":
        return 1
    return 0

def calculate_integral_value(y, x):
    number_above = 0
    number_left = 0
    number_diagonaly = 0

    if y > 0:
        number_above = integral_image[y - 1][x]

    if x > 0:
        number_left = integral_image[y][x - 1]

    if y > 0 and x > 0:
        # minus the diagonaly number its counted twice (no minus because of border of 0s)
        number_diagonaly = integral_image[y-1][x-1]
    
    return get_binary(data[y][x]) + number_left + number_above - number_diagonaly
        

def setup_data(data):
    global integral_image
    depth = len(data)
    length = len(data[0])

    for i, line in enumerate(data):
        line += "."
        data[i] = line

    row = ""
    for i in range(length + 1):
        row += "."
    data.append(row)

    integral_image = [[0 for x in range(length+1)] for y in range(depth+1)] 

def create_integral_grid():
    global integral_image
    global binary_index
    for lineIndex, _ in enumerate(data):
        for charIndex, char in enumerate(data[lineIndex]):
            if char == "@":
                binary_index.append((lineIndex, charIndex))

            integral_number = calculate_integral_value(lineIndex, charIndex)
            integral_image[lineIndex][charIndex] = integral_number

def read_integral(y , x, square_size):
    global p1
    number_above = 0
    number_left = 0
    number_diagonaly = 0

    # Top right corner of the square
    if y - (square_size - 1) >= 0:
        number_above = integral_image[y - (square_size - 1)][x + 1]

    # Bottom left corner of the square
    if x - (square_size - 1) >= 0:
        number_left = integral_image[y + 1][x - (square_size - 1)]

    # bottom right corner of the square
    if x - (square_size - 1) >= 0 and y - (square_size - 1) >= 0:
        number_diagonaly = integral_image[y - (square_size - 1)][x - (square_size - 1)]

    total = integral_image[y+1][x+1] - number_above - number_left + number_diagonaly

    if total < 5:
        row = ""
        for i, char in enumerate(data[y]):
            if i == x:
                row += "."
                continue
            row += char
        data[y] = row
        p1 += 1


setup_data(data)
create_integral_grid()
for binary in binary_index:
    read_integral(binary[0], binary[1], p1_grid_size)

print(p1)

p2 = p1
running = True
while running:
    binary_index = []
    create_integral_grid()
    p1 = 0
    for binary in binary_index:
        read_integral(binary[0], binary[1], p1_grid_size)
    p2 += p1
    if p1 == 0:
        running = False

print(p2)