from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project
from graded_book import Gradedbook
graded_book=Gradedbook
choice=""
while choice !="0":
     print("******* Student Grade Book system *******")
     print("1.Add student: ")
     print("2. Add course: ")
     print("3. Add Enroll student: ")
     print("4. Add Assessment: ")
     print("5. Record Grade ")
     print("6. Show Report")
     print("7. Search student:")
     print("8. Delete student: ")
     print("9. Dashboard: ")
     print("0. Exit")

     choice= input("Enter your a number: ")
     if choice =="1":
         name= input("Enter student name: ")
         Student_id=input("Enter student Id: ")
         email=input ("Enter student email: ")
         student=Student(name,student_id, email)
         graded_book.add_student(student)

     elif choice=="2":
         course_code=input("Enterr course code: ")
         course_name=input("Enter course name: ")
         course=Course(course_code,course_name)
         graded_book.add_course(course)

     elif choice=="3":
         student_id= input("Enter student Id: ")
         course_code=input("Enter course code: ")
         graded_book.enrol_student(student_id,course_code)
     elif choice=="4":
         course_code=input("Enter course code: ")
         print("A. Quiz!")
         print("B.Exam")
         print("C. project")
         assessment_type=input("Choose assessement type: ")
         title_type=input("Enter assessment title type: ")
         max_score=int(input("Enter maximum score: "))

         if assessment_type=="A":
             assessment=Quiz(title_type, max_score)
             






