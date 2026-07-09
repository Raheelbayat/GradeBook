class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score/ self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"

    def display_info(self):
        print(f"{self.title}- Max Score: {self.max_score}")