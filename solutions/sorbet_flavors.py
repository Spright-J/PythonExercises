
FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

def main():
    count = 0
    for flavor in FLAVORS:
        for flavor2 in range(count, len(FLAVORS)):
            if flavor == FLAVORS[flavor2]:
                continue
            print(flavor + ', ' + FLAVORS[flavor2])
        count +=1

if __name__ == "__main__":
    main()



'''
You're working for a restaurant and they're asking you to generate the sorbet menu.

Provide a script printing every possible sorbet duos from a given list of flavors.

Don't print recipes with twice the same flavor (no "Chocolate Chocolate"), and don't print twice the same recipe (if you print "Vanilla Chocolate", don't print "Chocolate Vanilla", or vice-versa).
'''