from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

gradebook = Gradebook()

student1 = Student("S001", "Ahmad Bayat", "ahmad@gmail.com", [])
student2 = Student("S002", "Munira Bayat", "MN123bayat@yahoo.com", [])

gradebook.add_student(student1)
gradebook.add_student(student2)

course1 = Course("NM01", "Neuromatch Computational Neuroscience Course")
gradebook.add_course(course1)

gradebook.enroll_student("S001", "NM01")
gradebook.enroll_student("S002", "NM01")
print(gradebook.students)
print(gradebook.courses)