list = []
filename = ' '

with open(filename, 'w') as file:
    for item in list:
        file.write("%s\n" % item)
        
print(filename)