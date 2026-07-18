class Graded_book:
    def __init__(self):
        self.student={}
        self.courses={}
        self.grade={}
        self.passing_grade=55
    def add_student(self,student):
        self.student[student.student_id]=student
    def add_course(self,course):
        self.courses[course.course_code]= course
    def add_grade(self,):