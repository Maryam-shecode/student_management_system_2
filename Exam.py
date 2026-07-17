from assessment import Assessment
class Exam(Assessment):
    def display_info(self):
        print("Exam: ", self.title, )
        print("Maximum score: ", self.max_score)
    def grade_message(self,score):
        percentage=self.calculate_percentage(score)
        if percentage 55>=

