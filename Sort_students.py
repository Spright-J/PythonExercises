def sort_by_mark(my_class):
    my_class = sorted(my_class, key=lambda student: student[0], reverse = True)
    return my_class


def sort_by_name(my_class):
    my_class = sorted(my_class, key=lambda student: student[1])
    return my_class


# Uncomment the following lines as needed
# if you want to test your implementation a bit:

my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

print(sort_by_mark(my_class))
# print(sort_by_name(my_class))




'''
Part 1
Write a function named sort_by_mark that take as argument a list of students and returns a copy of it sorted by mark in descending order. Such as:

>>> sort_by_mark(students)
[(85, "Susan"), (37, "Jeanette"), (6, "Joshua")]
Part 2
Write a function named sort_by_name that take as argument a list of students and returns a copy of it sorted by name in ascending order, such as:

>>> sort_by_name(students)
[(37, "Jeanette"), (6, "Joshua"), (85, "Susan")]
'''