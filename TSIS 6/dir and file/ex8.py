import os
file_path = " "
if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
    else:
        print("No access")  
else:
    print("No file")