major_colors = ["White", "Red", "Black", "Yellow", "Violet"] # Normalize strings for alignment
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_color_map():
    temp_list = []
    space = 6
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            interval = i * 5 + j + 1
            # Save the output into a list
            string = f'{interval}'.center(space)+'|'+f'{major}'.center(space)+'|'+f'{minor}'.center(space)+'|'
            temp_list.append(string) # Add 0 at start of number for alignment
    # Print color map codes
    print(*temp_list, sep = "\n")
    # Add a return value called "temp_list" that cointains the output
    return len(major_colors) * len(minor_colors), temp_list

# Define new function to test pair color code
def get_pair_number_from_color(major_color, minor_color):
    try:
        major_index = major_colors.index(major_color)
    except ValueError:
        # raise Exception('Major index out of range')
        return False
    try:
        minor_index = minor_colors.index(minor_color)
    except ValueError:
        # raise Exception('Minor index out of range')
        return False
    return major_index * len(minor_colors) + minor_index + 1


result, output = print_color_map()
#First evaluate the fullfield pair of colors
assert(result == 25)
for index, data in enumerate(output):
    expected_index, major_color, minor_color = data.split('|',2)
    # Check the first position in where are located the '|' separator inside the list
    if index == 0:
        first_separator_position = data.find('|')
    # Validate pair color string welformed
    pair_number = get_pair_number_from_color(major_color.strip(), minor_color.replace('|','').strip())
    assert(pair_number == int(expected_index.strip()))
    # Check alignment on next list elements using the first_separator_position
    assert(data.find('|') == first_separator_position)

print("All is well (maybe!)\n")
