
students = []

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })
    print("Student added successfully!")

def display_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student)

def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found:", student)
            return

    print("Student not found.")

while True:
    print("\n--- Student Record System ---")
    print("1. Add student")
    print("2. Display students")
    print("3. Search student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
