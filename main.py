from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

gradebook = Gradebook()


student1 = Student(
    "S001",
    "Ahmad Rahimi",
    "ahmad6456@gmail.com"
)

gradebook.add_student(student1)


course1 = Course(
    "Nm01",
    "Neuromatch"
)


gradebook.add_course(course1)


gradebook.enroll_student(
    "S001",
    "Nm01"
)


quiz1 = Quiz(
    "Quiz 1",
    10
)

midterm = Exam(
    "Midterm Exam",
    100
)

final_project = Project(
    "Final Project",
    100
)


gradebook.add_assessment(
    "Nm01",
    quiz1
)

gradebook.add_assessment(
    "Nm01",
    midterm
)

gradebook.add_assessment(
    "Nm01",
    final_project
)


gradebook.record_grade(
    "S001",
    "Nm01",
    "Quiz 1",
    10
)

gradebook.record_grade(
    "S001",
    "Nm01",
    "Midterm Exam",
    100
)

gradebook.record_grade(
    "S001",
    "Nm01",
    "Final Project",
    99
)
gradebook.delete_student("S001")
gradebook.show_report("S001")

gradebook.teacher_comment("S001", "Nm01")