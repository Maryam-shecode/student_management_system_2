from assessment import Assessment
class Quiz(Assessment):
    def display_info(self):
        print("Quiz: ", self.title)
        print("Maximum: ", self.max_score)
    def grade_message(self,score):
        percentage =self.calculate_percentage(score)
        if percentage>=90:
            return "Great Quiz"
        elif percentage>=80:
            return " Nice job"
        elif percentage>=70:
            return "well done"
        elif percentage>=60:
            return" you need more practice!"
        else:
            return" study hard!"

