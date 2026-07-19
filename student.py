class Student:
    def __init__(self, name, student_id, email):
        self.name=name
        self.student_id=student_id
        self.email=email
        self.courses=[]
    def display_info(self):
        print("Student ID: ", self.student_id)
        print(" Name: ", self.name)
        print(" Email Address: ", self.email)
    def get_id(self):
        return self.student_id
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def set_email(self, email):
        if "@" in email:
            self.email=email
            print("Email has been recorded successfully")
        else:
            print("invalid")
    def enrol_course(self, course_code):
        self.courses.append(course_code)


