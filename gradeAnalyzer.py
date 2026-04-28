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

