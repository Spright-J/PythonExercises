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

def sum_primes(limit):
    total = 0
    for num in range(0, limit):
        if is_prime(num):
            total += num
    return total


'''
Write a sum_primes function returning the sum of every prime number strictly inferior to its single parameter.

Example
>>> sum_primes(10)
17
Advice
You may copy/paste your is_prime function from a previous exercise ;)
'''