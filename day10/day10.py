data = open("./day10/input.txt", "r").read().splitlines()

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

def recursive_mask_gen(mask, button_wiring, index, masks):
    if index >= len(button_wiring) or mask in masks:
        return masks
    
    xor_result = xor_string(mask, button_wiring[index])
    masks.append(xor_result)

    return recursive_mask_gen(xor_result, button_wiring, index + 1, masks)
    
    




def pat1(data):
   
    for line in data:


        manual = line["manual"]
        masks = {}
        masks["0"] = manual
        masks["1"] = line["button_wirings"]

        button_wirings = recursive_mask_gen(manual, line["button_wirings"], 0, [])
        masks[str(i + 2)] = button_wirings




data = data_setup(data)
pat1(data)