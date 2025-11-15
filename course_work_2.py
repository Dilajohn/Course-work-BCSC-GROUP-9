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

# calculator.py
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