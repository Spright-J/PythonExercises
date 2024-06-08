def fibonacci(n): 
    if n < 1:
        fib_list = []
    elif n < 2:
        fib_list = [1]
    else:
        fib_list = [1,1]
    
    for num in range(1, n - 1):
        fib_list.append(fib_list[num - 1] + fib_list[num])

    return fib_list
