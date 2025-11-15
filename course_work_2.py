#QUESTION (4-5)=== COURSEWORK 2
"""  
AuthorS: OKUJA EMMANUEL DILA JOHN   2500728777  25/U//28777/PSA
         WASSWA KATEREGGA MAURICE   2500703613  25/U/03613/PSA
         NANFUKA JUSTINE            2500703528  25/U/03528/PS
         WAMIMBI CHRISTIAN          2500730993  25/U/30993/PSA

""" 
# Date: November 15, 2025

#QUESTION  4
""" 
v) How functions improve readability and reusability

Functions improve code in the following ways:
    *Modularity: Each operation is isolated  easy to test/debug.
    *Reusability: add() can be used anywhere, not just in calculator.
    *Readability: result = calc.add(x, y) ,is clearer than x + y in complex logic.
    *Maintainability: Fix divide() once and it affects all uses.
    *Abstraction: User sees calc.power(2, 3) (it's not 2**3)
    *Organization: Group related functions in modules (easier navigation)
"""

# calculator
import os
import math
import json
from datetime import datetime
from typing import Callable, Dict, List
class Calculator:
    def __init__(self):
        self.history: List[Dict] = []
        self.operation_map: Dict[str, Callable] = {
            '+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide,
            '^': self.power, 'sqrt': self.sqrt, 'sin': self.sin, 'cos': self.cos, 'tan': self.tan
        }
        self.load_history()

    #  Operations (iv) 
    def add(self, a: float, b: float) -> float: return a + b
    def subtract(self, a: float, b: float) -> float: return a - b
    def multiply(self, a: float, b: float) -> float: return a * b
    def divide(self, a: float, b: float) -> float:
        if b == 0: raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    def power(self, a: float, b: float) -> float: return a ** b
    def sqrt(self, a: float) -> float:
        if a < 0: raise ValueError("Cannot compute square root of negative number")
        return math.sqrt(a)
    def sin(self, a: float) -> float: return math.sin(math.radians(a))
    def cos(self, a: float) -> float: return math.cos(math.radians(a))
    def tan(self, a: float) -> float: return math.tan(math.radians(a))

    # Input & Execution (ii, iv) 
    def execute_operation(self, op: str, a: float, b: float = None) -> float:
        if op not in self.operation_map:
            raise ValueError("Unsupported operation")
        func = self.operation_map[op]
        try:
            if op in ['sqrt', 'sin', 'cos', 'tan']:
                result = func(a)
            else:
                result = func(a, b)
            self.log_calculation(op, a, b, result)
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

    def log_calculation(self, op: str, a: float, b: float, result: float):
        entry = {
            "operation": op,
            "input": [a, b] if b is not None else [a],
            "result": result,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.history.append(entry)
        self.save_history()

    #  File I/O (vi)
    def save_history(self): 
        # (Same as above)
        ...

    def load_history(self): 
        # (Same as above)
        ...

    def show_history(self):
        if not self.history:
            print("No history.")
            return
        print("\n=== Calculation History ===")
        for i, h in enumerate(self.history[-10:], 1):
            inp = " & ".join(map(str, h["input"]))
            print(f"{i}. {inp} {h['operation']} → {h['result']}")



#viii) You developed a CGPA software solution in your coursework. You are then tasked with
#creating and adding a secure system form that captures the student details in that
#application to authenticate users.

import hashlib

class SecureAuth:
    def __init__(self):
        self.users = self.load_users()

    def hash_password(self, password: str) : 
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, reg_no: str, name: str, password: str):
        if reg_no in self.users:
            print("User already exists!")
            return False
        self.users[reg_no] = {
            "name": name,
            "password_hash": self.hash_password(password)
        }
        self.save_users()
        print("Registration successful!")
        return True

    def login(self, reg_no: str, password: str): 
        if reg_no not in self.users:
            print("Invalid credentials.")
            return False
        stored_hash = self.users[reg_no]["password_hash"]
        if stored_hash == self.hash_password(password):
            print(f"Welcome, {self.users[reg_no]['name']}!")
            return True
        print("Invalid credentials.")
        return False

    def save_users(self):
        try:
            with open("users.json", "w") as f:
                json.dump(self.users, f)
        except: pass

    def load_users(self):
        try:
            with open("users.json", "r") as f:
                return json.load(f)
        except: return {}


#ix) What is the output of the piece of program below once it's corrected, completed and
#executed. Replace the student details with your own details
class Student:
    def __init__(self, reg_number, name, stud_number):
        self.reg_number = reg_number
        self.name = name
        self.stud_number = stud_number

    def print_student_details(self):
        print('name, regno, studeno', self.name, self.reg_number, self.stud_number)

class CS_Student(Student):
    course = 'Computer Science'

    def print_student_details(self):
        Student.print_student_details(self)
        print('Course:', CS_Student.course)


student1 = Student('25/U/28777/PSA', 'OKUJA EMMANUEL', 2500728777)
student2 = CS_Student('25/U/03613/PSA', 'WASSWA KATEREGGA MAURICE', 2500703613)      

student1.print_student_details()
student2.print_student_details()



#question 5
# q5_final_python.py
# Group 9 Final Submission
# Generates Final_Answers_Group9.docx with ALL Q1–Q4 outputs

from docx import Document
from docx.shared import Pt
from datetime import datetime

# ==============================
# CREATE DOCUMENT
# ==============================
doc = Document()

# ==============================
# GROUP HEADER
# ==============================
doc.add_heading('FINAL ANSWERS - QUESTIONS 1 TO 4', 0)
doc.add_paragraph("GROUP 9", style='Intense Quote')

authors = [
    "OKUJA EMMANUEL DILA JOHN      2500728777    25/U/28777/PSA",
    "WASSWA KATEREGGA MAURICE      2500703613    25/U/03613/PSA",
    "NANFUKA JUSTINE               2500703528    25/U/03528/PS",
    "WAMIMBI CHRISTIAN             2500730993    25/U/30993/PSA"
]

for author in authors:
    p = doc.add_paragraph(f"Author: {author}")
    p.runs[0].bold = True

doc.add_paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} EAT")
doc.add_paragraph("")

# ==============================
# QUESTION 1: CGPA + Basic Calculator
# ==============================
doc.add_heading('QUESTION 1: CGPA + Basic Calculator', 1)

# Basic Calculator Output
doc.add_heading('Basic Calculator Output', 2)
basic_text = """Student Numbers: 216022204, 216002204, 216007570, 216002774
Sum: 864034752
Extracted CUs: CU1=64, CU2=3, CU3=47, CU4=52

Results:
• Addition: 166
• Subtraction: -38
• Multiplication: 469248
• Division: 21.33"""
doc.add_paragraph(basic_text)

# CGPA Semester 1
doc.add_heading('CGPA Semester 1 Output', 2)
cgpa1_text = """CGPA Calculation Report
Student ID: 2500728777
Name: OKUJA EMMANUEL DILA JOHN
Semester: Semester 1
Date: 2025-11-15 12:45
CGPA: 5.0 → Distinction

Code | Course Name | Marks | Grade | GP | CU
CSK 1101 | COMMUNICATION SKILLS | 80.0 | A | 5.0 | 4
CSC 1102 | STRUCTURED AND OBJECT ORIENTED PROGRAMMING | 86.0 | A | 5.0 | 4
CSC 1104 | COMMPUTER ORGANIZATION AND ARCHITECTURE | 89.0 | A | 5.0 | 4
CSC 1105 | MATHEMATICS | 96.0 | A+ | 5.0 | 4

Formula Used:
CGPA = Σ(GPᵢ × CUᵢ) / ΣCUᵢ"""
doc.add_paragraph(cgpa1_text)

# CGPA Semester 2
doc.add_heading('CGPA Semester 2 Output', 2)
cgpa2_text = """CGPA Calculation Report
Student ID: 2500728777
Name: OKUJA EMMANUEL DILA JOHN
Semester: Semester 2
Date: 2025-11-15 12:52
CGPA: 5.0 → Distinction

Code | Course Name | Marks | Grade | GP | CU
CSC 1200 | OPERATING SYSTEMS | 89.0 | A | 5.0 | 4
CSC 1201 | PROBABILITY AND STATISTICS | 89.0 | A | 5.0 | 4
CSC 1202 | SOFTWARE DEVELOPMENT AND DESIGN | 85.0 | A | 5.0 | 4
IST 1204 | SYSTEMS ANALYSIS AND DESIGN | 90.0 | A+ | 5.0 | 4

Formula Used:
CGPA = Σ(GPᵢ × CUᵢ) / ΣCUᵢ"""
doc.add_paragraph(cgpa2_text)

doc.add_page_break()

# ==============================
# QUESTION 2: C Structure
# ==============================
doc.add_heading('QUESTION 2: C Structure Handling', 1)
q2_text = """a) Initialization:
struct course one;
one.cName = "Computer Architecture";
one.cCode = 1104;

b) User Input:
char buffer[100];
printf("Enter Course Name: ");
fgets(buffer, sizeof(buffer), stdin);
buffer[strcspn(buffer, "\\n")] = 0;
one.cName = malloc(strlen(buffer) + 1);
strcpy(one.cName, buffer);
scanf("%d", &one.cCode);

c) Pointer Access:
struct course* ptr = &one;
printf("Course Code via pointer: %d\\n", ptr->cCode);

d) Function Prototype:
void weThink(struct course c);"""
doc.add_paragraph(q2_text)

doc.add_page_break()

# ==============================
# QUESTION 3: Error Handling + OOP
# ==============================
doc.add_heading('QUESTION 3: Error Handling + OOP', 1)

q3a_text = """a) Division by Zero:
def calculate_average(amount_collected: int, number_of_users: int) -> float:
    try:
        average = amount_collected / number_of_users
        return average
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return 0.0"""
doc.add_paragraph(q3a_text)

q3b_text = """b) File Not Found:
try:
    with open("report.txt", "r") as file:
        content = file.read()
        print("File content:\\n", content)
except FileNotFoundError:
    print("File not found.")"""
doc.add_paragraph(q3b_text)

doc.add_heading('c) OOP Concepts', 2)
oop_text = """i. Inheritance
Inheritance allows a subclass to inherit from a superclass.
class Animal:
    def __init__(self, name): self.name = name
    def speak(self): print("The animal makes a sound.")
class Dog(Animal):
    def speak(self): print(f"{self.name} barks.")
my_dog = Dog("Buddy"); my_dog.speak()  # Output: Buddy barks.

ii. Encapsulation
Bundles data and methods with access control.
class BankAccount:
    def __init__(self, balance): self.__balance = balance
    def deposit(self, amount):
        if amount > 0: self.__balance += amount
    def get_balance(self): return self.__balance

iii. Polymorphism
Same interface, different behavior.
def make_animal_speak(animal): print(animal.speak())
make_animal_speak(Dog())  # Woof!
make_animal_speak(Cat())  # Meow!"""
doc.add_paragraph(oop_text)

doc.add_page_break()

# ==============================
# QUESTION 4: Calculator + Auth + Output
# ==============================
doc.add_heading('QUESTION 4: Calculator + Auth + Output', 1)

q4v_text = """v) Functions improve:
- Modularity: Isolated logic
- Reusability: add() used anywhere
- Readability: calc.add(x,y) clearer than x+y
- Maintainability: Fix once, affects all"""
doc.add_paragraph(q4v_text)

q4viii_text = """viii) Secure Authentication:
class SecureAuth:
    def hash_password(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()
    def login(self, reg_no: str, password: str) -> bool:
        # Secure hash comparison"""
doc.add_paragraph(q4viii_text)

q4ix_text = """ix) Output:
name, regno, studeno OKUJA EMMANUEL 25/U/28777/PSA 2500728777
name, regno, studeno WASSWA KATEREGGA MAURICE 25/U/03613/PSA 2500703613
Course: Computer Science"""
doc.add_paragraph(q4ix_text)

# ==============================
# SAVE DOCUMENT
# ==============================
filename = "Final_Answers_Group9.docx"
doc.save(filename)
print(f"{filename} generated successfully!")
