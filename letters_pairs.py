import string

def main():
    for letter in string.ascii_lowercase:
        for letter2 in string.ascii_lowercase:
            print(letter + letter2)


if __name__ =="__main__":
    main()

'''
Provide a script printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically.
'''