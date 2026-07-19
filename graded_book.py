class Gradedbook:
    def __init__(self):
        self.student={}
        self.courses={}
        self.grade={}
        self.passing_grade=55
    def add_student(self,student):
        self.student[student.student_id]=student
    def add_course(self,course):
        self.courses[course.course_code]= course
    def enroll_student(self, student_id, course_code):
        if student_id in self.student:
            if course_code in self.courses:
                self.student[student_id].enrol_course(course_code)
                print("student enrolled successfully.")
            else:
                print("course is not found")
        else:
            print("student is not found")
    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessement(assessment)
            print("Assessment is added")
        else:
            print("Course is not found!")
    def record_grade(self,student_id, course_code, assessment_title,score):
        if student_id not in self.grade:
            self.grade[student_id]={}
        student_grade =self.grade[student_id]
        if course_code not in self.grade[student_id]:
            self.grade[student_id][course_code]={}
        self.grade[student_id][course_code][assessment_title]={}
        print("Grade recorded successfully.")
    def calculate_average(self,student_id, course_code):
        score=self.grade[student_id][course_code].values()

        if len(score)==0:
            return 0
        average=sum(score)/len(score)
        return average
    def get_result(self,average):
        if average>=self.passing_grade:
            return "pass"
        else:
            return "failed"

    def show_report(self, student_id):
        student=self.student[student_id]
        print("Student: ",student.name)
        print("Student Id: ", student.student_id)
        for course in self.grade[student_id]:
            average =self.calculate_average(student_id,course)
            result=self.get_result(average)
            print("course")
            print("Average: ",average)
            print("Result: ", result)
    def search_student(self,keyword ):
        for student in self.student.values():
            if student.student_id == keyword:
                return student
            if student.name== keyword:
                return student
        return None
    def delete_student(self, student_id):
        if student_id in self.student:
            del self.student[student_id]
        if student_id in self.grade:
            del self.grade[student_id]
        print("student deleted!")

    def dashboard(self):
        total_assessment=0
        for course in self.courses.values():
            total_assessment= total_assessment+len(course.assessments)
        print("Total Students: ", len(self.student))
        print("Total courses: ", len(self.courses))
        print("Total Assessment: ", total_assessment)

