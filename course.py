class Course:
    def __init__(self,course_code, course_name):
        self.course_code=course_code
        self.course_name=course_name
        self.students=[]
        self.assessments=[]
    def add_student(self,student_id):
        self.students.append(student_id)
    def add_assessment (self, assessment):
        self.assessments.append(assessment)
    def find_assessment(self,title):
        for assessment in self.assessments:
            if assessment.title==title:
                return assessment
        return None
    def display_info(self):
        print("Course code: ", self.course_code)
        print("Course name: ", self.course_name)
        print("Students: ", self.students)
        print("Assessments: ")
