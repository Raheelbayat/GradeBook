from main import Student

class Course:
    def __init__(self, course_code, course_name, students, assessments):
        self.course_code = course_code
        self.course_name = course_name
        self.students = students
        self.assessments = assessments

    def add_student(student_id):
        pass

    def add_assessment(assessment):
        pass

    def find_assessment(title):
        for assessment in assessments:
            if assessment['title'] == title:
                return assessment
            else:
                return None

    def display_info():
        print(f"Course code: {self.course_code}\n"
              f"Course Name: {self.course_name}\n"
              f"Enrolled Students: {self.students}")

