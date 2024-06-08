import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_range(lower, upper):
    primes = [str(num) for num in range(lower, upper) if is_prime(num)]
    return ", ".join(primes)

print(prime_range(10000,10050))

'''
Provide a script that print every prime number in the range [10000;10050], on one line, separated by comas and spaces.

The output (in the range [1;10]) should look like this:

$ python3 solution.py
2, 3, 5, 7

'''