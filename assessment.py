class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score/ self.max_score) * 100

    def grade_message(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def display_info(self):
        print(f"{self.title}- {self.max_score}%")
        # percentage = self.calculate_percentage(self.score)
        # grade = self.grade_message(percentage)
        #
        # print(f"Assessment: {self.title}")
        # print(f"Max Score: {self.max_score}")
        # print(f"Score: {self.score}")
        # print(f"Percentage: {percentage:.2f}%")
        # print(f"Grade: {grade}")