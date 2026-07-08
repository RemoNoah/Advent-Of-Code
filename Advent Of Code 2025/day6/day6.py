data = open("./day6/input.txt", "r").read().splitlines()

input = []
# 1 1 1 1
# 2 3 3 1 
# 1 7 8 1
# + * * +


for line in data[:-1]:
    line_numbers = [int(x) for x in line.split()]
    input.append(line_numbers)

input.append([x for x in data[-1].split()])


def calculate_checksum(column_number, operation):
    sum = 0
    for i, line in enumerate(input[:-1]):
        if i == 0:
            sum = input[i][column_number]
            continue
        
        if operation == "+":
            sum += input[i][column_number]
        elif operation == "*":
            sum *= input[i][column_number]
    return sum

p1 = 0

for col in range(len(input[0])):
    p1 += calculate_checksum(col, input[-1][col])

print("Part 1:", p1)

def rotate_data(data):
    return list(zip(*data))[::-1]


def part_two(rotated_data):
    p2 = 0

    problem_count = 1
    
    for n in rotated_data:
        if ("".join(n[:-1])).strip() == "":
            problem_count += 1

    for j in range(problem_count):
        sum = 0


        number_count = 0
        for n in rotated_data:
            if ("".join(n[:-1])).strip() != "":
                number_count += 1
            else:    
                break


        operation = rotated_data[number_count-1][-1]

        # iterate through each line count to know how many numbers to multiply/add
        for i in range(number_count):
            if i == 0:
                sum = int("".join(rotated_data[0][:-1]))
                rotated_data.pop(0)
                continue
            if operation == "+":
                sum += int("".join(rotated_data[0][:-1]))
            elif operation == "*":
                sum *= int("".join(rotated_data[0][:-1]))
            rotated_data.pop(0)
        p2 += sum
        if len(rotated_data) > 0:
            rotated_data.pop(0)

    print("Part 2:", p2)
    
part_two(rotate_data(data))
