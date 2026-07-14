from assessment import Assessment

class Project(Assessment):
    def display_info(self):
        print(f"Your Scores detailed_info is:\n"
              f"Project Title: {self.title}, Max Score: {self.max_score}")

    def grade_message(self, score):
        if score >= 90:
            return f"Perfect Project!"
        elif score >= 80:
            return f"Great Project!"
        elif score >= 70:
            return f"Excellent Project!"
        elif score >= 50:
            return f"Needs small changes! Try a bit more."
        elif score <= 40:
            return f"Please, Try again! Project needs improvement!"