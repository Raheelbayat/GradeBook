import student


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

    def add_course(self, course):
        self.courses[course.course_code] = course

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

        total_percentage = 0
        number_of_existing_scores = 0

        if student_id not in self.students:
            print("Student not found")
            return

        if course_code not in self.courses:
            print("Course not found")
            return

        course = self.courses[course_code]

        for key, score in self.grades.items():

            if key[0] == student_id and key[1] == course_code:

                assessment_title = key[2]

                for assessment in course.assessments:

                    if assessment.title == assessment_title:
                        percentage = assessment.calculate_percentage(score)

                        total_percentage += percentage
                        number_of_existing_scores += 1
                        break

        if number_of_existing_scores == 0:
            print("No score found")
            return

        return total_percentage / number_of_existing_scores

    def get_letter_grade(self, average):
        if average >= 95:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found")
            return

        student = self.students[student_id]
        print("\n\n")
        print("===== Student Report =====")
        print("\n")
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.full_name}")
        print(f"Email: {student.email}")

        total_percentage = 0
        number_of_scores = 0
        print("\n\n")
        for course_code in student.courses:

            course = self.courses[course_code]

            print(f"Course: {course.course_code} - {course.course_name}")
            print("\n\n")
            print("Grades:")

            for key, score in self.grades.items():

                if key[0] == student_id and key[1] == course_code:

                    assessment_title = key[2]

                    for assessment in course.assessments:
                        if assessment.title == assessment_title:
                            percentage = assessment.calculate_percentage(score)

                            print(
                                f"{assessment_title}: {score}/{assessment.max_score} = {percentage:.0f}%"
                            )

                            total_percentage += percentage
                            number_of_scores += 1
                            break
        print("\n\n")
        if number_of_scores == 0:
            print("No grades available")
            return

        average = total_percentage / number_of_scores

        print(f"Average: {average:.2f}%")

        letter_grade = self.get_letter_grade(average)

        if average >= self.passing_grades:
            result = "Passed"
        else:
            result = "Failed"

        print(f"Average: {average:.2f}%")
        print(f"Letter Grade: {letter_grade}")
        print(f"Result: {result}")

    def search_student(self, studentterm):
        if studentterm in self.students:
            return self.students[studentterm]

        for student in self.students.values():
            if student.full_name == studentterm:
                return student

        print("Student not found")

    def delete_student(self, student_id):
        def delete_student(self, student_id):
            if student_id not in self.students:
                print("Student not found")
                return

        student = self.students[student_id]
        for course_code in student.courses:
            if course_code in self.courses:
                course = self.courses[course_code]
                if student_id in course.students:
                    course.students.remove(student_id)
        del self.students[student_id]

    def get_result(self, average):
        if average >= self.passing_grades:
            return "Passed"
        else:
            return "Failed"

    def teacher_comment(self, student_id, course_code):

        if student_id not in self.students:
            print("Student not found")
            return

        average = self.calculate_average(student_id, course_code)

        student = self.students[student_id]

        letter_grade = self.get_letter_grade(average)

        if letter_grade == "A" or letter_grade == "B":
            print(f"I am really proud of you!")

        elif letter_grade == "C":
            print(f"Good effort, keep improving.")

        else:
            print(f"Keep practicing. I am sure, you can perform much better!")
