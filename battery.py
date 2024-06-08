def battery_charge(charge):
    charge_round = round(charge, -1)
    print_charge = ['[',]
    count = 0
    while charge_round != 0:
        print_charge.append('❚')
        charge_round -= 10
        count += 1
    while count < 10:
        print_charge.append(' ')
        count += 1
    print_charge.append(']')
    print(''.join(print_charge))
    print('{}%'.format(charge))


battery_charge(75)