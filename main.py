from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

gb = Gradebook()

student1 = Student("S001", "Ahmad Rahimi", "ahmad@example.com", [])
student2 = Student("S002", "Sara Ali", "sara@example.com", [])

gb.add_student(student1)
gb.add_student(student2)

