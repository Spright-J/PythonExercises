def get_3_5(start, stop):
    return_nums = []
    for num in range(start, stop):
        if num % 3 == 0 or num % 5 == 0:
            return_nums.append(num)
    return return_nums

def main():
    sum_nums = 0
    for num in get_3_5(0,1000):
        sum_nums += num
    print(sum_nums)

if __name__ == "__main__":
    main()

'''
Write a program that finds the sum of all natural numbers below 1000 (< 1000) that are multiples of 3 or 5, and prints it.

If we list all the natural numbers below 20 (<20) that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, 18. The sum of these multiples is 78.

Note that 15 is only counted once.
'''