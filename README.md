## Name: Maryam Bigzad
## Project title: Student management system 
### Project description: 

 The project is a student management system which is developed by using Python and OOP. It allows users to manage students, courses, assessments, and also grades. In this system we can add students, courses, and also enroll students in courses. We can add assessments, records grades and also calculate their average grades. We are also able to search students, delete and show the dashboard. 
### How to run this system?
1. Open the project in PyCharm or any Python IDE.
2. Run the `main.py` file.
3. Follow the menu displayed on the screen.
4. Enter the required information for each option.
### There are Seven class:
a. Student
b. Course
c. Assessment
d. Quiz
e. Exam
f  Project
g. Gradebook
## Encapsulation
Encapsulation is used by keeping the data and functions together inside each class.

Student stores student details.
Course stores course details.
Assessment stores assessment details.
Gradebook manages all the system's tasks and operations.

## Inheritance
There is a parent which is the Assessment class.
there are three other class which is child class that inherits from parent.
Inheritance is used between:
Quiz → Assessment 
Exam → Assessment
Project → Assessment

## Method Overriding
This method is used in these three class Quiz,Exam, and Project class
each class provides its own grading message

## Custom Features
###  Update Student Name
The user can update a student's name by entering the Student ID.
###  Dashboard
The dashboard displays:
- Total number of students
- Total number of courses
- Total number of assessments