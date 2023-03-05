import re

def to_camel(string):
    camel = re.sub(pat, lambda matching: matching.group(1).upper(), string)
    return camel

string = "hello_world"
pat = r"_([a-z])"
print(to_camel(string))