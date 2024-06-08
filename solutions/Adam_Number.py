def check_adam_number(num):
    
    flip_num = str(num)[::-1]

    num_square = num * num
    flip_num_square = int(flip_num) * int(flip_num)
    
    reg_flip_num = str(flip_num_square)[::-1]

    if num_square == int(reg_flip_num):
        return True
    else:
        return False

    


print(check_adam_number(22))

