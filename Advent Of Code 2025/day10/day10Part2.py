data = open("./Advent Of Code 2025/day10/input.txt", "r").read().splitlines()
testdata = open("./Advent Of Code 2025/day10/testInput.txt", "r").read().splitlines()

def create_binary_manuals(data):
    return data.replace("#", "1").replace(".", "0").replace("[", "").replace("]", "")
        

def create_binary_button_wiring(data, length):
    data = data.replace("(", "").replace(")", "")
    button_wirings = [int(x) for x in data.split(",")]
    
    binary  = "0" * length
    for i in button_wirings:
        binary = binary[:i] + "1" + binary[i+1:]

    list = []
    for char in binary:
        list.append(int(char))

    return tuple(list)


def data_setup(data): 
    cleaned_data = []

    for line in data:
        split_line = [x for x in line.split(" ")]
        manual = create_binary_manuals(split_line[0])

        cleaned_line = {}
        cleaned_line["manual"] = manual

        button_wirings = []

        for buttons in split_line[1:-1]:
            button_wiring = create_binary_button_wiring(buttons, len(manual))
            button_wirings.append(button_wiring)
        
        cleaned_line["button_wirings"] = button_wirings
        cleaned_data.append(cleaned_line)

        cleaned_line["joltage"] = [int(x) for x in split_line[-1].replace("{","").replace("}", "").split(",")]

    return cleaned_data


def add_button_wiring(current_joltage, button_wiring):
    new_joltage = []
    for i, char in enumerate(current_joltage):
        new_joltage.append(char + button_wiring[i])

    return tuple(new_joltage)


def part2(data):
    sum_tries = 0
    canceled = 0
    found = 0

    for line in data:
        joltage = tuple(line["joltage"])
        masks = []
        masks.append(line["joltage"])
        masks.append((line["button_wirings"]))
        presses = 1
        
        if joltage in line["button_wirings"]:
            print(f"Found manual {str(joltage)} with 1")
            sum_tries += 1
            continue
        
        is_found = False
        print("--------------------")
        print("Searching: " + str(joltage))
        print(found)
        print("--------------------")
        while not is_found:

            print("Presses" + str(presses))

            new_joltages = set()

            for button in masks[1]:
                for other_button in masks[presses]:
                    new_joltage = add_button_wiring(button, other_button)

                    is_higher = False
                    for i, char in enumerate(new_joltage):
                        if char > joltage[i]:
                            is_higher = True
                            break


                    if not is_higher:
                        if not new_joltage in new_joltages:
                            if new_joltage == joltage:
                                is_found = True
                                print(f"Found manual {joltage} with {len(masks)}")
                                sum_tries += len(masks)
                                break

                            new_joltages.add(new_joltage)
                        else: 
                            canceled += 1
                
                if is_found:
                    found += 1
                    break

            masks.append(new_joltages)
            presses += 1
    
    print(f"Total tries: {sum_tries}")
    print(f"Total canceled: {canceled}")
    return sum_tries 


#data = data_setup(data)
data = data_setup(testdata)


part2(data)