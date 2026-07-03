student = {}

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

    def set_email(self, email):
        if "@" in email and "." in email:
            self.email = email
            print("Email updated successfully.")
        else:
            print("Invalid email address.")


    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
            print(f"{course_code} enrolled successfully.")
        else:
            print(f"{course_code} is already enrolled.")


    def display_info(self):
        print(f"\nStudent ID: {self.student_id}"
              f"\nFull name: {self.full_name}"
              f"\nEmail: {self.email}")

        if self.courses:
            print("Courses:", ", ".join(self.courses))
        else:
            print("Courses: No courses enrolled")

