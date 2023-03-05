import re
string = input()
pat = "[a-z][_]"
if re.search(pat, string):
    print("found")
else:
    print("not found")