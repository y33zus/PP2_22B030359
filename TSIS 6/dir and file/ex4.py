inpfile = " "
with open(inpfile, 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    print("The file has", num_lines, "lines.")