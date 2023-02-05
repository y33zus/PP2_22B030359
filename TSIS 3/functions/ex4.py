def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes=[]
    for x in range(len(numbers)):
        if is_prime(numbers[x]):
            primes.append(numbers[x])
    return primes
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))