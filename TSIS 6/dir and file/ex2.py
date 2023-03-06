import os
path = " "
if os.access(path, os.R_OK) and os.access(path, os.X_OK) and os.access(path, os.W_OK):
    print("You have access")
else:
    print("You do not have access")