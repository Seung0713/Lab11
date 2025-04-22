import os
import matplotlib.pyplot as plt

# Load data
def load_students(file_path):
    students = {}
    with open(file_path, 'r') as f:
        for line in f:
            name, id_str = line.strip().rsplit(' ', 1)
            students[id_str] = name
    return students

def load_assignments(file_path):
    assignments = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().rsplit(' ', 2)
            name = parts[0]
            point_value = int(parts[1])
            assignment_id = parts[2]
            assignments[assignment_id] = (name, point_value)
    return assignments

def load_submissions(file_path):
    submissions = {}  # key = (student_id, assignment_id), value = percent
    with open(file_path, 'r') as f:
        for line in f:
            student_id, assignment_id, percent = line.strip().split()
            submissions[(student_id, assignment_id)] = float(percent)
    return submissions

# Load all data files
students = load_students('data/students.txt')
assignments = load_assignments('data/assignments.txt')
submissions = load_submissions('data/submissions.txt')

# Show menu
print("1. Student grade")
print("2. Assignment statistics")
print("3. Assignment graph\n")
choice = input("Enter your selection: ")

if choice == "1":
    name_input = input("What is the student's name: ").strip()
    student_id = None
    for sid, name in students.items():
        if name.lower() == name_input.lower():
            student_id = sid
            break

    if not student_id:
        print("Student not found")
    else:
        total_score = 0
        for aid, (aname, points) in assignments.items():
            percent = submissions[(student_id, aid)]
            total_score += (percent / 100) * points
        grade_percent = round((total_score / 1000) * 100)
        print(f"{grade_percent}%")

elif choice == "2":
    assignment_input = input("What is the assignment name: ").strip()
    assignment_id = None
    points = None
    for aid, (aname, pts) in assignments.items():
        if aname.lower() == assignment_input.lower():
            assignment_id = aid
            points = pts
            break

    if not assignment_id:
        print("Assignment not found")
    else:
        scores = [submissions[(sid, assignment_id)] for sid in students]
        print(f"Min: {int(min(scores))}%")
        print(f"Avg: {int(sum(scores) / len(scores))}%")
        print(f"Max: {int(max(scores))}%")

elif choice == "3":
    assignment_input = input("What is the assignment name: ").strip()
    assignment_id = None
    for aid, (aname, _) in assignments.items():
        if aname.lower() == assignment_input.lower():
            assignment_id = aid
            break

    if not assignment_id:
        print("Assignment not found")
    else:
        scores = [submissions[(sid, assignment_id)] for sid in students]
        plt.hist(scores, bins=[0, 25, 50, 75, 100])
        plt.title(f"{assignment_input} Score Distribution")
        plt.xlabel("Score Percent")
        plt.ylabel("Number of Students")
        plt.show()

else:
    print("Invalid selection.")
