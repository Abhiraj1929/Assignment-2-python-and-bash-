student_grades = {
    "Alice": 88,
    "Bob": 76,
    "Charlie": 92
}

def print_menu():
    print("\n--- Student Grade Manager ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    print("-----------------------------")

def add_student():
    name = input("Enter the new student's name: ")
    if name in student_grades:
        print(f"Error: {name} already exists. Use the update option instead.")
        return
    try:
        grade = int(input(f"Enter {name}'s grade: "))
        student_grades[name] = grade
        print(f"Successfully added {name} with a grade of {grade}.")
    except ValueError:
        print("Invalid grade. Please enter a number.")

def update_grade():
    name = input("Enter the name of the student to update: ")
    if name not in student_grades:
        print(f"Error: Student '{name}' not found.")
        return
    try:
        new_grade = int(input(f"Enter the new grade for {name}: "))
        student_grades[name] = new_grade
        print(f"Successfully updated {name}'s grade to {new_grade}.")
    except ValueError:
        print("Invalid grade. Please enter a number.")

def print_all_grades():
    if not student_grades:
        print("No student grades to display.")
        return
    print("\n--- Current Student Grades ---")
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")
    print("------------------------------")


if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_grade()
        elif choice == '3':
            print_all_grades()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")
