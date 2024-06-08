def mul(numbers):
    answer = numbers[0]
    for num in numbers[1::]:
        answer = answer * num
    return answer


'''
Write a function called mul taking a single iterable argument.

The function have to multiply all values from the given iterable.

As an example mul([1, 2, 3]) should compute 1 × 2 × 3.

It is not usefull to use print in this kind of functions (you can still, for debugging purpose), better use return so the result is given back to the caller, and can be used again.
'''