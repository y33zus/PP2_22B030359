input_string = input()
uppercase_count = 0
lowercase_count = 0
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)