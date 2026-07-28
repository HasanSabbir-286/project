Student Grade Manager

A command-line Student Grade Manager built with Python.

This project allows users to manage student records using a JSON file for permanent storage. You can add, view, search, and delete student records, as well as find the highest-scoring student(s).

Features:

➕ Add new students

📋 View all student records

🔍 Search students by name

🔍 Search students by mark

🏆 Find the highest mark and display all students who achieved it

🗑️ Delete student records by name or mark

💾 Automatically save data to a JSON file

✅ Input validation for names, marks, and menu choices

🚫 Prevent duplicate student names


Project Structure:

student-grade-manager/ │── student_grade_manager.py │── student_directory.json └── README.md 

Requirements

Python 3.x

No external libraries are required.

How to Run

Clone the repository:

git clone <repository-url> 

Navigate to the project folder:

cd student-grade-manager 

Run the program:

python student_grade_manager.py 

Data Storage:

Student records are stored in: student_directory.json 

The data remains available even after closing the program.

Example Student Record

{ "students": [ { "name": "Alice", "mark": 95 }, { "name": "Bob", "mark": 87 } ] } 

Skills Practiced

Python Functions

Loops

Conditional Statements

Exception Handling

Lists and Dictionaries

JSON File Handling

CRUD Operations (Create, Read, Update, Delete)

Input Validation

Modular Programming

Future Improvements

Update student marks

Sort students by name or mark

Calculate average mark

Find the lowest mark

Export records to CSV

Build a graphical user interface (GUI)

Author:

Created by Hasan Sabbir as a Python practice project.