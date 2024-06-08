def select_student(students, threshold):
    acc_list = []
    den_list = []

    for index in students:
        if index[1] >= threshold:
            acc_list.append(index)
        else:
            den_list.append(index)
    
    acc_list = sorted(acc_list, key=lambda student: student[1], reverse = True)
    den_list = sorted(den_list, key=lambda student: student[1])

    return {"Accepted": acc_list, "Refused": den_list}

'''
Write a function telling appart accepted and refused students according to a threshold.

The function should be called select_student and takes as arguments:

A list where each element is a list of a student name, and his grade.
A grade. The student grade must be superior or equal to the given grade to be accepted.
Your function must return a dictionnary with two entries:

Accepted which list the accepted students sorted by grades in the descending order.
Refused which list the refused students sorted by grades in ascending order.
'''