
def print_even_numbers(start, stop):
    for num in range(start, stop):
        if num % 2 == 0:
            print(num)
           


'''
Write a function printing every even numbers in the given range, one number per line.

Your function have to be named print_even_numbers and accept two parameters named start and stop.

Like Python's range, you'll have to start searching for even numbers by including start but excluding stop, remember:

for i in range(0, 10):
    print(i)

'''