import re

string = input()
pat = '[A-Z]+[a-z]+$'

if re.search(pat, string):
    print("FOUND!")
else:
    print("NOT FOUND!")