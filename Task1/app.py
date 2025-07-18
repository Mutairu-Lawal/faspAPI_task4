import json
import os
from student import Student

DATA_FILE = "data.json"


def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [Student.from_dict(item) for item in data]
    return []


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump([s.to_dict() for s in students], file, indent=4)


def add_student(students):
    name = input("Enter student name: ")
    subjects = {}
    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        score = float(input(f"Enter score for {subject}: "))
        subjects[subject] = score
    student = Student(name, subjects)
    students.append(student)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        print("\nName:", student.name)
        print("Subjects and Scores:", student.subjects)
        print("Average:", round(student.average, 2))
        print("Grade:", student.grade)


def update_student(students):
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student.name.lower() == name.lower():
            print("Student found. Updating subjects.")
            new_subjects = {}
            while True:
                subject = input("Enter subject (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                score = float(input(f"Enter score for {subject}: "))
                new_subjects[subject] = score
            student.subjects = new_subjects
            student.average = student.calculate_average()
            student.grade = student.calculate_grade()
            print("Student updated.")
            return
    print("Student not found.")


def main():
    students = load_students()
    while True:
        print("\n--- Student Report Card App ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
            save_students(students)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
