with open("words.txt", "r") as file:
    for line in file:
        print(line)
    file.close()

'''
Warning

It's better to try this exercise with your own installation of Python, on your computer. Learn how for Mac OSX or Windows.

Write a program which reads and prints the content of the words.txt file. That's all. I'll put the file is in the same directory as your code, so no absolute path required, just "words.txt" (or "./words.txt").
'''