from assessment import Assessment
class Exam(Assessment):
    def display_info(self):
        print(f"Your Scores detailed_info is:\n"
              f"Exam Title: {self.title}, Max Score: {self.max_score}")

    def grade_message(self, score):
        if score >= 55:
            return f"Great job! You Passed."
        elif score <= 54:
            return f"Try again! You Failed!"