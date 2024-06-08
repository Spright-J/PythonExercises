import string

def main():
    for letter in string.ascii_lowercase:
        for letter2 in string.ascii_lowercase:
            if letter == letter2:
                continue
            print(letter + letter2)

if __name__ =="__main__":
    main()

'''
Provide a script printing every possible pairs of two different letters.

Only lower case, one pair per line, ordered alphabetically.

Don't print pairs consisting of twice the same letter, such as 'aa', 'bb', etc...
'''