class Assessment:
    def __init__(self, title, max_score):
        self.title=title
        self.max_score=max_score
    def calculate_percentage(self,score):
        percentage=(score/self.max_score)*100
        return percentage
    def grade_message(self,score):
        percentage=self.calculate_percentage(score)
        if percentage>=90:
            return "Excellent!"
        elif percentage>=80:
            return "Nice"
        elif percentage>=70:
            return "Good"
        else:
            return" You need to study hard! "
        