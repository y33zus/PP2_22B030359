def div(n):
    list = [i for i in range(n) if i % 3 == 0 and i % 4 == 0]
    return list
n = int(input())
print(div(n))