class Student:
    def __init__(self, name, studend_Id, email):
        self.name=name
        self.studend_Id=studend_Id
        self.email=email
    def display_innfo(self):
        print("Student ID: ", self.studend_Id)
        print(" Name: ", self.name)
        print(" Email Address: ", self.email)
    def get_id(self):
        return self.studend_Id
    
