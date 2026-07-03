from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz

score = 0

s1 = Student("S101", "Mohammad Karim", "Karimmoh12@gmail.com", ["Quran", "Math"])
s1.display_info()
s2 = Student("S002", "Ahmad Murtazawi", "Qaramurteaza@yahoo.com", ["German"] )
s2.display_info()



percentage = Assessment.calculate_percentage(self, 8)
score += percentage

print(f"Your score is: {percentage}%")
print(Assessment.grade_message(percentage))



