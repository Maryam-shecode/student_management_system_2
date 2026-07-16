from assessment import Assessment
class Quiz(Assessment):
    def desplay_Info(self):
        print("Quiz: ", self.title)
        print("Maximum score: ",self.max_score)