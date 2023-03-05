import re

string = input()
pat = 'ab{2,3}?'

if re.match(pat, string):
    print("FOUND!")
else:
    print("NOT FOUND!")