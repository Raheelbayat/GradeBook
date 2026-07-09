import student
from student import Student
from course import Course
from assessment import Assessment
from exam import Exam


class Gradebook:
    def __init__(self):
        self.students = {}  # Bcz my dictionaries are empty I didnt write them as parameters.
        self.courses = {}
        self.grades = {}
        self.passing_grades = 55

    def add_student(self, student):
        # self.students.append(student) #remember that in dictionaries, I cannot use append! It is for lists!
        self.students[student.student_id] = student  # self.students is my dictionary
        # student.student_id: take the ID inside the student object
        # =student: update and put it into the student variable

    def add_course(self, course_code):
        course = self.courses[course_code]

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students:
            print(f"No Student found")
            return
        # if course_code not in self.courses: as  I have already asked above, so I might not repeat it.
        #     return "Course not found"

        current_student_info = self.students[student_id]

        if course_code not in current_student_info.courses:
            current_student_info.courses.append(course_code)
            print(f"{student_id} is enrolled in {course_code}")
        else:
            print(f"{student_id} is already enrolled in {course_code}")

    def add_assessment(self, course_code, assessment):
        if course_code not in self.courses:
            print(f"No course found")
            return  # I should keep in mind that if I write return instead of print to make the code shorter
        # the code will run and if the course dont found among course list then it will just return none without any message: no course found.

        course = self.courses[course_code]
        course.assessments.append(assessment)
        print(f"{assessment.title} added to {course_code}")

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            print(f"Student not found")
            return

        if course_code not in self.courses:
            print(f"Course not found")
            return
        course = self.courses[course_code]
        # here I will check if assessment exist:
        assessment_found = None
        for assessment in course.assessments:
            if assessment.title == assessment_title:
                assessment_found = assessment
                break

        if assessment_found is None:
            print("Assessment not found")
            return

        if score < 0 or score > assessment_found.max_score:
            print("Invalid score")
            return

        # here we saved the information in the score variable
        self.grades[(student_id, course_code, assessment_title)] = score
        print("Grade is recorded successfully.")

    def calculate_average(self, student_id, course_code):
        total_score = 0
        number_of_existing_scores = 0
        for key, score in self.grades.items():
            if key[0] == student_id and key[1] == course_code:
                total_score += score
                number_of_existing_scores += 1

        if student_id not in self.students:
            print(f"No student found for {course_code}")
            return
        if number_of_existing_scores == 0:
            print(f"No score found for {course_code}")
            return

        average_score = total_score / number_of_existing_scores
        return average_score

    def show_report(self, student_id):
        student = self.students[student_id]
        print(student.full_name)


        # if student_average >= self.passing_grades:
        #     print(f"Passed!")
        #     if student_average >= 95:
        #         print("A")
        #     elif student_average >= 80:
        #         print("B")
        #     elif student_average >= 70:
        #         print("C")
        #     elif student_average >= 60:
        #         print("D")
        #     else:
        #         print("F")
        #     return
        # else:
        #     print(f"Failed!")
        #     return
