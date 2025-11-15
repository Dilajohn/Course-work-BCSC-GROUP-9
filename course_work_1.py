# cgpa_calculator.py
# Author: Group Member (Teamwork Encouraged)
# Date: November 15, 2025
# Purpose: CGPA Calculator + Basic Calculator with File I/O and Word Export

import os
from datetime import datetime
from docx import Document
from docx.shared import Pt
from typing import List, Dict, Tuple


GRADE_TO_GP = {
    'A+': 5.0, 'A': 5.0,
    'B+': 4.5,
    'B': 4.0,
    'C+': 3.5,
    'C': 3.0,
    'D+': 2.5,
    'D': 2.0,
    'E': 1.5,
    'E-': 1.0,
    'F': 0.0
}

MARKS_TO_GRADE = {
    (90, 100): 'A+',
    (80, 89): 'A',
    (75, 79): 'B+',
    (70, 74): 'B',
    (65, 69): 'C+',
    (60, 64): 'C',
    (55, 59): 'D+',
    (50, 54): 'D',
    (45, 49): 'E',
    (40, 44): 'E-',
    (0, 39): 'F'
}



class StudentCGPA:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.history = []  # List of semester records
        self.load_history()

    

    def input_semester_data(self) -> Dict:
        print(f"\n--- Entering Data for {self.name} ({self.student_id}) ---")
        courses = []
        for i in range(4):
            print(f"\nCourse Unit {i+1}:")
            code = input("  Course Code: ").strip().upper()
            name = input("  Course Name: ").strip()
            marks = float(input("  Marks (0-100): ").strip())
            cu = int(input("  Credit Units: ").strip())
            grade = self.marks_to_grade(marks)
            gp = GRADE_TO_GP[grade]
            courses.append({
                'code': code,
                'name': name,
                'marks': marks,
                'grade': grade,
                'gp': gp,
                'cu': cu
            })
        return {'courses': courses, 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")}

    

    def marks_to_grade(self, marks: float) -> str:
        for (low, high), grade in MARKS_TO_GRADE.items():
            if low <= marks <= high:
                return grade
        return 'F'

    def calculate_cgpa(self, semester_data: Dict) -> float:
        total_gp_cu = 0.0
        total_cu = 0
        for course in semester_data['courses']:
            total_gp_cu += course['gp'] * course['cu']
            total_cu += course['cu']
        return round(total_gp_cu / total_cu, 2) if total_cu > 0 else 0.0

    def classify_cgpa(self, cgpa: float) -> str:
        if cgpa >= 4.5:
            return "Distinction"
        elif cgpa >= 2.0:
            return "Pass"
        else:
            return "Fail"

    
    def get_filename(self) -> str:
        return f"cgpa_history_{self.student_id}.txt"

    def save_history(self):
        filename = self.get_filename()
        try:
            with open(filename, 'w') as f:
                for record in self.history:
                    f.write(f"{record['semester']}|{record['cgpa']}|{record['classification']}|{record['timestamp']}\n")
            print(f"CGPA history saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_history(self):
        filename = self.get_filename()
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    for line in f:
                        parts = line.strip().split('|')
                        if len(parts) == 4:
                            self.history.append({
                                'semester': parts[0],
                                'cgpa': float(parts[1]),
                                'classification': parts[2],
                                'timestamp': parts[3]
                            })
                print(f"Loaded {len(self.history)} previous records.")
            except Exception as e:
                print(f"Error loading file: {e}. Starting fresh.")

    
    def add_semester(self, semester_name: str):
        data = self.input_semester_data()
        cgpa = self.calculate_cgpa(data)
        classification = self.classify_cgpa(cgpa)
        record = {
            'semester': semester_name,
            'cgpa': cgpa,
            'classification': classification,
            'timestamp': data['timestamp'],
            'courses': data['courses']
        }
        self.history.append(record)
        self.save_history()
        self.generate_word_report(record)
        print(f"\nCGPA for {semester_name}: {cgpa} → {classification}")

    
    def generate_word_report(self, record: Dict):
        doc = Document()
        doc.add_heading('CGPA Calculation Report', 0)
        doc.add_paragraph(f"Student ID: {self.student_id}")
        doc.add_paragraph(f"Name: {self.name}")
        doc.add_paragraph(f"Semester: {record['semester']}")
        doc.add_paragraph(f"Date: {record['timestamp']}")
        doc.add_paragraph(f"CGPA: {record['cgpa']} → {record['classification']}\n")

        # Table
        table = doc.add_table(rows=1, cols=6)
        hdr_cells = table.rows[0].cells
        headers = ['Code', 'Course Name', 'Marks', 'Grade', 'GP', 'CU']
        for i, h in enumerate(headers):
            hdr_cells[i].text = h
            hdr_cells[i].paragraphs[0].runs[0].font.bold = True

        for course in record['courses']:
            row = table.add_row().cells
            row[0].text = course['code']
            row[1].text = course['name']
            row[2].text = str(course['marks'])
            row[3].text = course['grade']
            row[4].text = str(course['gp'])
            row[5].text = str(course['cu'])

        # Formula
        doc.add_paragraph("\nFormula Used:")
        doc.add_paragraph("CGPA = Σ(GPᵢ × CUᵢ) / ΣCUᵢ", style='Intense Quote')

        filename = f"CGPA_Report_{self.student_id}_{record['semester'].replace(' ', '_')}.docx"
        try:
            doc.save(filename)
            print(f"Report saved as {filename}")
        except Exception as e:
            print(f"Error saving Word document: {e}")


def basic_calculator() -> Dict:
    # Student numbers
    students = [216022204, 216002204, 216007570, 216002774]
    total = sum(students)
    print(f"Sum of student numbers: {total}")

    # Extract CU values: remove leftmost '8' → 64034752 → CU1=64, CU2=03, CU3=47, CU4=52
    num_str = str(total).lstrip('8')  # Remove leading 8
    cu_values = [int(num_str[i:i+2]) for i in range(0, len(num_str), 2)]
    cu1, cu2, cu3, cu4 = cu_values[:4]

    operations = {
        'Addition': cu1 + cu2 + cu3 + cu4,
        'Subtraction': cu1 - cu2 - cu3 - cu4,
        'Multiplication': cu1 * cu2 * cu3 * cu4,
        'Division': round(cu1 / cu2, 2) if cu2 != 0 else "Error (div by 0)"
    }

    print("\nBasic Calculator Results:")
    for op, result in operations.items():
        print(f"  {op}: {result}")

    return {
        'student_numbers': students,
        'sum': total,
        'extracted_cus': [cu1, cu2, cu3, cu4],
        'operations': operations
    }


def main():
    print("=== CGPA & BASIC CALCULATOR SYSTEM ===\n")

    # --- Basic Calculator ---
    calc_results = basic_calculator()

    # --- CGPA Calculator ---
    print("\n" + "="*50)
    student_id = input("Enter your Student ID: ").strip()
    name = input("Enter your Name: ").strip()
    student = StudentCGPA(student_id, name)

    # Add two semesters
    for sem in ["Semester 1", "Semester 2"]:
        print(f"\n>>> Adding {sem} <<<")
        student.add_semester(sem)
        input("\nPress Enter to continue to next semester...")

    # Display history
    print("\n" + "="*50)
    print("CGPA HISTORY")
    for rec in student.history:
        print(f"{rec['semester']}: {rec['cgpa']} ({rec['classification']})")

    # Save basic calculator to Word too
    doc = Document()
    doc.add_heading('Basic Calculator Report', 0)
    doc.add_paragraph(f"Student Numbers: {', '.join(map(str, calc_results['student_numbers']))}")
    doc.add_paragraph(f"Sum: {calc_results['sum']}")
    doc.add_paragraph(f"Extracted CUs: CU1={calc_results['extracted_cus'][0]}, CU2={calc_results['extracted_cus'][1]}, "
                      f"CU3={calc_results['extracted_cus'][2]}, CU4={calc_results['extracted_cus'][3]}")
    doc.add_paragraph("\nResults:")
    for op, res in calc_results['operations'].items():
        doc.add_paragraph(f"• {op}: {res}")
    doc.save("Basic_Calculator_Report.docx")
    print("Basic calculator report saved as Basic_Calculator_Report.docx")

if __name__ == "__main__":
    main()