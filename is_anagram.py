def is_anagram(left, right):
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters == right_letters

def main():
    is_anagram("poop","poop")

if __name__ =="__main__":
    main()


'''
I've written a function called is_anagram.

This function takes two parameters:

left: it expects just one word, as a Python str.
right: it also expects just one word, as a Python str.
the function should return True if the two words are anagrams, False otherwise.

Sadly there's a small error in my implementation (try to submit it if you don't catch it), can you fix it?

Just in case you messed with the code too much and want to start fresh, here it is:
'''
