import re

string = input()
pat = r"a(b*)"

if re.match(pat, string):
    print("FOUND!")
else:
    print("NOT FOUND!")