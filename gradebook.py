class Gradebook:
    def __init__(self, students, courses, grades, passing_grades):
        self.students = students
        self.courses = courses
        self.grades = grades
        self.passing_grades = passing_grades

    def add_student(self, student):
        self.students.append(student)



