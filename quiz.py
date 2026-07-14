from assessment import Assessment

class Quiz(Assessment):
    def display_info(self):
        print(f"Your Scores detailed_info is:\n"
              f"Quiz Title: {self.title}, Max Score: {self.max_score}")

    def grade_message(self, score):
        percentage  = self.calculate_percentage(score)
        if percentage >= 95:
            return "Great job!"
        elif percentage >= 80:
            return "Very good job!"
        elif percentage >= 70:
            return "Good job!"
        elif percentage >= 60:
            return "Not that Bad!"
        else:
            return "Please, Try more!"