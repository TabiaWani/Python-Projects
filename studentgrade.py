student_grade = {}

def add_student(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")
    
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"Updated {name} with a {grade}")
    else:
        print(f"{name} not found")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} not found")

def display_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name}: {grade}")
    else:
        print("No students found")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. Display students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter student's name: ")
            grade = int(input("Enter student's grade: "))
            add_student(name, grade)
        
        elif choice == 2:
            name = input("Enter student's name: ")
            grade = int(input("Enter new grade: "))
            update_student(name, grade)
        
        elif choice == 3:
            name = input("Enter the name you want to delete: ")
            delete_student(name)
        
        elif choice == 4:
            print("YOUR STUDENTS NAME WITH MARKS")
            display_all_students()
        
        elif choice == 5:
            print("Closing the program")
            break
        
        else:
            print("Invalid choice, please try again.")

# Call the main function to start the program
main()
