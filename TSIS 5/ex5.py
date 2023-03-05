import re
string = input()
pat = 'a.*?b$'

if re.match(pat, string):
    print("found")
else:
    print("not found")