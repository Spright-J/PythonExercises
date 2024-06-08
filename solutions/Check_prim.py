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


'''
Define the function is_prime(n).

n is number that the function is_prime takes as a parameter.

The function is_prime return True if n is a prime number, False otherwise. Such as:

Examples
>>> from solution import is_prime
>>> is_prime(1)
False
>>> is_prime(2)
True
>>> is_prime(3)
True
>>> is_prime(4)
False
'''