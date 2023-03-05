import re
string = input()
pat = "[ ,.]"
print(re.sub(pat,":", string))