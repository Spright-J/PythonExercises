def print_even_numbers(start, stop):
    return_nums = []
    for num in range(start, stop):
        if num % 2 == 0:
            return_nums.append(num)
    return return_nums

def main():
    sum_nums = 0
    for num in print_even_numbers(0,101):
        sum_nums += num
    print(sum_nums)


if __name__ == "__main__":
    main()

'''
Provide a script that prints the sum of every even numbers in the range [0; 100].

'''