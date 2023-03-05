import re
pat = r"(\w)([A-Z])"
string = input()
print(re.sub(pat, r"\1 \2", string))