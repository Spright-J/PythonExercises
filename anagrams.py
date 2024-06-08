import unicodedata


def is_anagram(left, right):
    left = ''.join(char.lower() for char in unicodedata.normalize('NFD', left) if unicodedata.category(char) != 'Mn' and char.isalnum())
    right = ''.join(char.lower() for char in unicodedata.normalize('NFD', right) if unicodedata.category(char) != 'Mn' and char.isalnum())
    
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    
    return sorted_left == sorted_right

  


print(is_anagram("ab", "aba"))



'''
Write a simple function, named is_anagram, taking two strings, and returning a boolean value.

The function shall return True if the letters of one word are a rearrangement of the letters of the other, False otherwise.

Superfluous (or missing) spaces, quotes, dashes, ... are allowed: funeral is an anagram of real fun.

Capitalized letter are equivalent to lower case letters: Madam Curie is an anagram of Radium came.

Diactirics of any language are ignored: crâné is an anagram of crane.
'''