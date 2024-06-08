def how_to_pay(amount, currency):
    currency.sort(reverse=True)
    payment_dict = {}
    
    for coin in currency:
        count = amount // coin
        if count > 0:
            payment_dict[coin] = count
            amount -= coin * count
    
    if amount > 0:
        return None
    
    return payment_dict



euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
print(how_to_pay(50, euro)) # expected == {1: 50}


'''
Write a function named how_to_pay taking two parameters: amount and currency.

amount is an amount to pay.
currency describe the currency as a list of existing coins or banknotes.
The function should return a dict describing the easiest way to pay amount with the given currency.

For example, to pay 3 with a currency having coins of [1, 2, 5] you have to use one coin of 2 and one coin of 1, so the function should return {2: 1, 1: 1}.
'''