from math import tan, pi
side = int(input())
length = float(input())
area = (side * (length ** 2)) / (4 * tan(pi / side))
print(area)