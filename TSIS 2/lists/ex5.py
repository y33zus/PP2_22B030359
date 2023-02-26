fruits = ["apple", "watermelon", "che"]
# fruits.sort()
b = sorted(fruits, key=lambda a: len(a) > 3)
# fruits.remove("banana")
print(b)