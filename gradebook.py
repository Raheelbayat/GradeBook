from student import Student
from course import Course
from assessment import Assessment

class Gradebook:
    def __init__(self):
        self.students = {} #Bcz my dictionaries are empty I didnt write them as parameters.
        self.courses = {}
        self.grades = {}
        self.passing_grades = 55

    def add_student(self, student):
        # self.students.append(student) #remember that in dictionaries, I cannot use append! It is for lists!
        self.students[student.student_id] = student  #self.students is my dictionary
        #student.student_id: take the ID inside the student object
        # =student: update and put it into the student variable

    def add_course(self, course):
        self.courses[course.course_code] = course

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students:
            return "No Student found"

        # if course_code not in self.courses: as  I have already asked above, so I might not repeat it.
        #     return "Course not found"

        student = self.students[student_id]

        if course_code not in student.courses:
            student.courses.append(course_code)
            print(f"{student_id} is enrolled in {course_code}")
        else:
            print(f"{student_id} is already enrolled in {course_code}")

        # def add_assessment(self, course_code, assessment):
        #     #Check!
        #     assessment.[course_code] = course

        # def record_grade(self, student_id, course_code, assessment, title, score):
        #     if student_id not in self.students:
        #         return "Student not found"
        #
        #     if course_code not in self.courses:
        #         return "Course not found"
        #     course = self.courses[course_code]
        #
        #     if title not in course.assessments:
        #         return "Assessment not found"
        #
        #     key = student_id + "_" + course_code
        #     if key not in self.grades:
        #         self.grades[key] = {}
        #     self.grades[key][title] = score
        #     print(f"{student_id} got {score} in {title} ({course_code})")


gradebook = Gradebook()
s1 = Student("S001", "Maria", "ali@email.com", [])
gradebook.add_student(s1)