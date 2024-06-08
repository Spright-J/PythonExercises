for num in range(1000):
    digit_sum = sum(int(digit) for digit in str(num))
    if num % 7 == 0 and digit_sum % 3 == 0:
        print(num)



'''
Create a program to find and print all numbers between from 0 to 1000 (both included), that are divisible by 7 and whose digits sum are divisible by 3.

For instance, 1512 is divisible by 7 and the sum of all is digits is 9 and is divisible by 3.
'''