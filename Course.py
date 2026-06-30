from main import Student

class Course:
    def __init__(self, course_code, course_name, students, assessments):
        self.course_code = course_code
        self.course_name = course_name
        self.students = students
        self.assessments = assessments

    def add_student(student_id):