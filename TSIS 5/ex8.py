import re
string = input()
shablon = "[A-Z]"
print(re.findall('[A-Z][^A-Z]*', string))