def longest_word(text):
    text_split = text.split()
    big_word = ""
    for word in text_split:
        if len(word) > len(big_word):
            big_word = word
    return big_word

text = "Monty Python and the Holy Grail"
print(longest_word(text))


'''
Write a function giving the longest word in a given text.

Your function should be named longest_word, take a single argument text and return a string which should be the longest word in the given text.

Beware: the given text can span several lines.
'''