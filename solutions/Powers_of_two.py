def main():
    numbers = [*range(0,10)]
    for num in numbers: 
        print(2 ** num)

if __name__ == "__main__":
    main()



'''
Print the 10 first powers of two, one per line. (beware: not the first squares!)

Start at 0, so the first power of two is 20 (which happen to be one), followed by 21, 22, and so on up to 29.

As a reminder, the power operator in Python is written **, so:

>>> 2 ** 5
32
'''