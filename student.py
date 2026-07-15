class Student:
    def __init__(self, name, studend_Id, email):
        self.name=name
        self.studend_Id=studend_Id
        self.email=email
        self.courses=[]
    def display_innfo(self):
        print("Student ID: ", self.studend_Id)
        print(" Name: ", self.name)
        print(" Email Address: ", self.email)
    def get_id(self):
        return self.studend_Id
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
    def enroll_course(self, course_code):
        self.courses.append(course_code)


