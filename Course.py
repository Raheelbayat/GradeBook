class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = [] #I did not add them in parameters category up above because they are lists and no need to add something that is empty.
        self.assessments = []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    def add_assessment(self, assessment):
        if assessment not in self.assessments:
            self.assessments.append(assessment)

    def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
        return None #why out of the loop I brought this? # Only after all assessments have been checked return None
            #return None     If I write the return none inside the loop, it will end the loop only after evaluating the first item.
    def display_info(self):
        print(f"Course code: {self.course_code}\n"
              f"Course Name: {self.course_name}\n"
              f"Enrolled Students: {len(self.students)}") #len() shows number of students

        print("Assessments:")
        for assessment in self.assessments:
            print(f"Assessment: {assessment.title} / Max Score: {assessment.max_score}")

