from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project
from graded_book import Gradedbook
graded_book=Gradedbook()
choice=""
while choice !="0":
     print("******* Student Grade Book system *******")
     print("1. Add student: ")
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
         student_id=input("Enter student Id: ")
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
         title_type=input("Enter assessment title: ")
         max_score=int(input("Enter maximum score: "))

         if assessment_type=="A":
             assessment=Quiz(title_type, max_score)
         elif assessment_type=="B":
             assessment=Exam(title_type,max_score)
         elif assessment_type=="C":
             assessment=Project(title_type,max_score)
         else:
             print("Invalid Type")
         graded_book.add_assessment(course_code,assessment)
     elif choice=="5":
         student_id=input("Enter student Id: ")
         course_code=input("Enter course code: ")
         assessment_title=input("Enter assessment title: ")
         score=int(input("Enter score: "))
         graded_book.record_grade(student_id,course_code,assessment_title,score)
     elif choice=="6":
         student_id=input("Enter student Id: ")
         graded_book.show_report(student_id)
     elif choice =="7":
         keyword=input("Enter student name or Id:")
         student=graded_book.search_student(keyword)
         if student is not None:
             student.display_info()
         else:
             print("studnet not found.")
     elif choice=="8":
         student_id=input("Enter student Id: ")
         graded_book.delete_student(student_id)
     elif choice =="9":
         graded_book.dashboard()
     elif choice =="10":
         student_id=input("Enter your Id: ")
         student=graded_book.search_student(student_id)
         if student !=None:
             update_name=input("Enter your update name: ")
             student.name=update_name
             print("student name successfully updated! ")
         else:
             print("student is not found")


     elif choice =="0":
         print("Program ended!")
     else:
         print("Invalid choice!")








