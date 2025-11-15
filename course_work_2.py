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


#Question 5
#python code
# generate_report.py
# Generates a complete Word document with outputs from Q1 to Q4
# Includes updated Q3(c) and full Q4 calculator

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime
import os

# ==============================
# Helper: Add section with title and content
# ==============================
def add_section(doc, title, content, is_code=False, language=""):
    p = doc.add_paragraph()
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(14)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    if is_code:
        para = doc.add_paragraph()
        para.paragraph_format.space_before = Pt(6)
        para.paragraph_format.space_after = Pt(6)
        para.paragraph_format.left_indent = Inches(0.5)
        run = para.add_run(content)
        run.font.name = 'Courier New'
        run.font.size = Pt(10)
        if language:
            lang_note = doc.add_paragraph(f"// Language: {language}", style='Caption')
            lang_note.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    else:
        for line in content.split('\n'):
            if line.strip():
                doc.add_paragraph(line, style='Normal')

    doc.add_page_break()

# ==============================
# Main Document Generation
# ==============================
def generate_python_report():
    doc = Document()
    doc.add_heading('COURSEWORK 1 AND 2 2025NOV - FULL REPORT', 0)
    doc.add_paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')} EAT")
    doc.add_paragraph("Student: Kizza Moses | Reg No: 2025/U/123 | ID: 216022204\n", style='Intense Quote')

    # === QUESTION 1: CGPA + Basic Calculator ===
    q1_code = '''# CGPA Calculator with File I/O and Word Export
class StudentCGPA:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.history = []
        self.load_history()

    def calculate_cgpa(self, courses):
        total_gp_cu = sum(c['gp'] * c['cu'] for c in courses)
        total_cu = sum(c['cu'] for c in courses)
        return round(total_gp_cu / total_cu, 2) if total_cu else 0.0

    def add_semester(self, semester_name):
        # Input 4 courses...
        cgpa = self.calculate_cgpa(courses)
        self.history.append({"semester": semester_name, "cgpa": cgpa})
        self.generate_word_report()

def basic_calculator():
    students = [216022204, 216002204, 216007570, 216002774]
    total = sum(students)
    num_str = str(total).lstrip('8')
    cu = [int(num_str[i:i+2]) for i in range(0, 8, 2)]
    return cu  # [64, 3, 47, 52]
'''
    add_section(doc, "QUESTION 1: CGPA + Basic Calculator", q1_code, is_code=True, language="Python")

    # === QUESTION 2: C Struct ===
    q2_code = '''struct course one;
one.cName = "Data Structures";
one.cCode = 1204;

char buffer[100];
printf("Enter Course Name: ");
fgets(buffer, sizeof(buffer), stdin);
one.cName = strdup(buffer);

struct course* ptr = &one;
printf("Code: %d", ptr->cCode);

void weThink(struct course c);'''
    add_section(doc, "QUESTION 2: C Structure Handling", q2_code, is_code=True, language="C")

    # === QUESTION 3: Error Handling + OOP ===
    q3_oop = '''i. Inheritance
Inheritance allows a subclass to inherit attributes/methods from a superclass.
class Animal:
    def __init__(self, name): self.name = name
    def speak(self): print("The animal makes a sound.")
class Dog(Animal):
    def speak(self): print(f"{self.name} barks.")
my_dog = Dog("Buddy"); my_dog.speak()  # Buddy barks.

ii. Encapsulation
Bundles data and methods; hides internal state.
class BankAccount:
    def __init__(self, balance): self.__balance = balance
    def deposit(self, amount):
        if amount > 0: self.__balance += amount
    def get_balance(self): return self.__balance
account = BankAccount(100); account.deposit(50)

iii. Polymorphism
Same interface, different behavior.
def make_animal_speak(animal): print(animal.speak())
make_animal_speak(Dog())  # Woof!
make_animal_speak(Cat())  # Meow!'''
    add_section(doc, "QUESTION 3(c): OOP Concepts (Updated)", q3_oop, is_code=True, language="Python")

    # === QUESTION 4: Full Calculator Class ===
    q4_full = '''class Calculator:
    def __init__(self):
        self.history = []
        self.ops = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide,
                    '^': self.power, 'sqrt': self.sqrt}

    def add(self, a, b): return a + b
    def divide(self, a, b):
        if b == 0: raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def execute(self, op, a, b=None):
        result = self.ops[op](a, b if b is not None else a)
        self.history.append(f"{a} {op} {b if b else ''} = {result}")
        return result

    def save_history(self):
        with open("calc_history.json", "w") as f:
            json.dump(self.history, f)

# Secure Login
class SecureAuth:
    def login(self, id, pwd):
        return hashlib.sha256(pwd.encode()).hexdigest() == stored_hash

# Output of Student Demo
name, regno, studeno Kizza Moses 2025/U/123 216022204
name, regno, studeno Nakato Sarah 2025/U/124 216002774
Course: Computer Science'''
    add_section(doc, "QUESTION 4: Full Calculator + Auth + Output", q4_full, is_code=True, language="Python")

    # Save
    filename = "Coursework_1_and_2_Report.docx"
    doc.save(filename)
    print(f"Report generated: {filename}")

if __name__ == "__main__":
    generate_python_report()