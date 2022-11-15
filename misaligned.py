
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            # I decide to implement an assert to use the current string
            # to check first '|' character position and save it into
            # a variable that are use to compare the next index position
            # and know if map is aligned or not
            pair_color_string = f'{i * 5 + j} | {major} | {minor}'
            if (i == 0) and (j == 0):
                first_separator_position = pair_color_string.find('|')
            assert(pair_color_string.find('|') == first_separator_position)
            print(pair_color_string)
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 25)

print("All is well (maybe!)\n")
