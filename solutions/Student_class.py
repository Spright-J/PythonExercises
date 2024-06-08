class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_exam(self, grade):
        self.grades.append(float(grade))

    def get_mean(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_mean(self):
        if not self.students:
            return 0.0
        return sum(student.get_mean() for student in self.students) / len(self.students)

    def get_best_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.get_mean())

class City:
    def __init__(self, name):
        self.name = name
        self.schools = []

    def add_school(self, school):
        self.schools.append(school)

    def get_mean(self):
        if not self.schools:
            return 0.0
        return sum(school.get_mean() for school in self.schools) / len(self.schools)

    def get_best_school(self):
        if not self.schools:
            return None
        return max(self.schools, key=lambda school: school.get_mean())

    def get_best_student(self):
        if not self.schools:
            return None
        best_students = [school.get_best_student() for school in self.schools if school.get_best_student() is not None]
        if not best_students:
            return None
        return max(best_students, key=lambda student: student.get_mean())