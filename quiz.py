from assessment import Assessment

class Quiz(Assessment):
    def display_info(self):
        print(f"Your Scores detailed_info is:\n"
              f"Title: {self.title}- Max Score: {self.max_score}")

    def grade_message(self, score):
        if score >= 90:
            return f"Great job! You got {self.max_score} points, which is over 90."
        elif score >= 80:
            return f"Very good job! You got {self.max_score} points, which is over 80."
        elif score >= 70:
            return f"Good job! You got {self.max_score} points, which is over 70."
        elif score >= 60:
            return f"Not that Bad! You got {self.max_score} points, which is less than 70."
        else:
            return (f"Please, Try more! You got {self.max_score} points, which is lower than the required score for "
                    f"passing tp the next grade.")