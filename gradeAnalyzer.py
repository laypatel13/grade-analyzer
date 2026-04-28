import csv
import os
import numpy as np

def load_grades(filename):
    if not os.path.exists(filename):
        print("File Not Found!")
        return None, None
    with open(filename, "r") as f:
        content = f.read()
        if content.strip() == "":
            return None, None
        rows = list(csv.reader(content.splitlines()))
    header = rows[0]
    data = rows[1:]

    return header, data

def analyze_students(data):  
    results = []

    for row in data:
        name = row[0]                                           
        grades = np.array([float(g) for g in row[1:]])        
        
        print(f"\n{name}")
        print(f"  Average : {np.mean(grades):.2f}")
        print(f"  Best    : {np.max(grades):.2f}")
        print(f"  Worst   : {np.min(grades):.2f}")
        
        results.append((name, np.mean(grades))) 


    print("\n--- Student Rankings ---")
    results.sort(key=lambda x: x[1], reverse=True)
    for rank, (name, avg) in enumerate(results, start=1):
        print(f"  {rank}. {name} - {avg:.2f}")

def analyze_subjects(data, header):
    subjects = header[1:]   

    for i, subject in enumerate(subjects):

        column = np.array([float(row[i+1]) for row in data])
            
        print(f"\n{subject.upper()}")
        print(f"  Class Average : {np.mean(column):.2f}")
        print(f"  Highest       : {np.max(column):.2f}")
        print(f"  Lowest        : {np.min(column):.2f}")

def flag_failing(data):
    print("\n--- Students Needing Attention ---")
    found = False

    for row in data:
        name = row[0]
        grades = np.array([float(g) for g in row[1:]])
        
        if np.any(grades < 40) :
            print(f"  {name} - failing in one or more subjects")
            found = True
    
    if not found:
        print("  No failing students!")

def main():
    file_name = input("Enter your file name: ")
    headers, data = load_grades(file_name)
    if data is None:
        return

    while True:
        print("\n----Grade Analyzer----")
        print("1. Analyze students")
        print("2. Analyze subjects")
        print("3. Flag failing students")
        print("4. Quit")

        try:
            user_input = int(input("Enter your response: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if user_input == 1:
            analyze_students(data, headers)
        elif user_input == 2:
            analyze_subjects(data, headers)
        elif user_input == 3:
            flag_failing(data, headers)
        elif user_input == 4:
            print("Exited...!")
            break
        else:
            print("Invalid Input...!")