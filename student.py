class Student:
    def __init__(self, name, studend_Id, email):
        self.name=name
        self.studend_id=studend_Id
        self.email=email
        self.courses=[]
    def display_info(self):
        print("Student ID: ", self.studend_id)
        print(" Name: ", self.name)
        print(" Email Address: ", self.email)
    def get_id(self):
        return self.studend_id
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


