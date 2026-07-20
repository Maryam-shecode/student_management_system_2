from assessment import Assessment
# child class
class Project(Assessment):
    def display_info(self):
        print("Project: ", self.title)
        print("Maximum score: ", self.max_score)
    def grade_message(self,score):
        percentage =self.calculate_percentage(score)
        if percentage>=95:
            return "Excellent Job!"
        elif percentage>=85:
            return "well done"
        elif percentage>=75:
            return "project submitted"
        else:
            return "project needs improvement"



