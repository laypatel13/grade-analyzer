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