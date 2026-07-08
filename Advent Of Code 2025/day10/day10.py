data = open("./Advent Of Code 2025/day10/input.txt", "r").read().splitlines()

def create_binary_manuals(data):
    return data.replace("#", "1").replace(".", "0").replace("[", "").replace("]", "")
        

def create_binary_button_wiring(data, length):
    data = data.replace("(", "").replace(")", "")
    button_wirings = [int(x) for x in data.split(",")]
    
    binary  = "0" * length

    for i in button_wirings:
        binary = binary[:i] + "1" + binary[i+1:]

    return binary


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

        cleaned_line["joltage"] = split_line[-1]

    
    return cleaned_data


def xor_string(s1, s2):
    result = ""

    for i, char in enumerate(s1):
        new = bool(int(char)) != bool(int(s2[i]))
        result += "1" if new else "0"
    return result


def pat1(data):
   
    for line in data:

        manual = line["manual"]
        masks = []
        masks.append(manual)
        masks.append((line["button_wirings"]))
        
        if manual in line["button_wirings"]:
            print(f"Found manual {manual} with 1")
            continue
        
        is_found = False
        
        while not is_found:
            new_masks = []
            for i, button in enumerate(masks[len(masks) - 1]):
                
                already_seen = [item for sublist in masks[1:] for item in sublist]
                already_seen.insert(0, "0" * len(manual))
                
                for other_button in line["button_wirings"][i+1:]:
                    xor_result = xor_string(button, other_button)
                    if not xor_result in already_seen:
                        new_masks.append(xor_result)
                
                        if xor_result == manual:
                            is_found = True
                            print(f"Found manual {manual} with {len(masks)}")
                            break
                
                if is_found:
                    break
            masks.append(new_masks)




data = data_setup(data)
pat1(data)