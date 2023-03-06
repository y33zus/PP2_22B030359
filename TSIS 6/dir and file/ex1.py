import os
path = " "
items = os.listdir(path)
for item in items:
    if os.path.isdir(os.path.join(path, item)) and os.path.isfile(os.path.join(path, item)):
        print(item)