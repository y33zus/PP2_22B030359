def is_prime(n):
    if n == 1:
        return False
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        return True
    else:
        return True
list = [1,2,3,4,5,6,7,8,9,10,11]

nonprime = filter(lambda x: is_prime(x), list)
print(list(nonprime))