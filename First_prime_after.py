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


def next_prime(n):
    while is_prime(n) == False:
        n += 1

    return n

print(next_prime(100000000))



'''
Provide a script that computes, then prints the first prime number greater than 100_000_000.

Advice
You may use itertools.count(), and you may need sys.exit().
'''