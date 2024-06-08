import string

def main():
    print("Gonna knock three times:")
    for i in range(3):
        print("*knock*")
    print("- Who's there?")

if __name__ == "__main__":
    main()



'''
In the given snippet, there's a bug: there's no indentation.

Your goal is to fix it (by just adding 4 spaces at the right place).

The code should display:

Gonna knock three times:
*knock*
*knock*
*knock*
- Who's there?
'''