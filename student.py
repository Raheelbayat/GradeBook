class Student:
    def __init__(self, student_id, full_name, email, courses):
        self.student_id = student_id
        self.full_name = full_name
        self.email = email
        self.courses = courses

    def get_id(self):
        return self.student_id

    def get_full_name(self):
        return self.full_name

    def set_email(self):
        self.email = self.full_name

    def set_email(email):
        email += email

    def enroll_course(course_code):
        self.courses.append(course_code)  #would not work! first make the course code dictionary or list then try


    def display_info(self):
        print(f"Student ID: {self.student_id}"
              f"\nFull name: {self.full_name}"
              f"\nEmail: {self.email}"
              f"\nEnrolled Courses: {self.enroll_course}")

s1 = Student("S101", "Mohammad Karim", "Karimmoh12@gmail.com", ["", ""])
s1.display_info()
