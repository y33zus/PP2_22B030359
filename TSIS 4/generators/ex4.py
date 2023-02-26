n = int(input())
m = int(input())
list = [i ** 2 for i in range(n, m+1)]
for i in range(len(list)):
    print(list[i])