import os
path = " "
if os.path.exists(path):
    print(path, "exists.")
    dirname, filename = os.path.split(path)
    print("Directory portion:", dirname)
    print("Filename portion:", filename)
else:
    print(path, "does not exist.")