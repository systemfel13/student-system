students = [
    {"name": "Tobias Fors", "email": "tobias.fors@yh.nackademin.se", "age": 30,  "student_id": 11230, "grades": {"Pythonprogrammering 1": 1, "Databasteknik": 4}},
    {"name": "Karin Börjell", "email": "karin.borjell@yh.nackademin.se", "age": 32,  "student_id": 11231, "grades": {"Pythonprogrammering 1": 1, "Pythonprogrammering 2": 3}},
    {"name": "Daniel Eliasson", "age": 29,  "email": "daniel.eliasson@yh.nackademin.se", "student_id": 11233, "grades": {"Pythonprogrammering 1": 1, "Affärsmannaskap": 2}},
    {"name": "Magdalena Andersson", "age": 50,  "email": "magdalena.andersson@yh.nackademin.se", "student_id": 11234, "grades": {"Pythonprogrammering 1": 1, "Webbramverk inom python": 5}},
]

def list_students_menu(students: list[dict]):
    for index, student in enumerate(students, start=1): # Loops through all the students and lists them from 1 instead of 0
        print(f"{index}. Name: {student["name"]}, Student-ID: {student["student_id"]}")

    while True:
        student_menu_users_choice = input("\nChoose a student or press Q to go back: ")
        if student_menu_users_choice.lower().strip() == "q":
            break

# Converting users choice to an int
        try:
            student_index = int(student_menu_users_choice)
        except ValueError:
            print("Invalid choice. Please enter a number from the list.")
            continue

# Checks if the users choice is a student in the list
        try:
            selected_student = students[student_index - 1]
        except IndexError:
            print("There is no student with that number. Please try again.")
            continue

# Loop with menu choices for the selected student
        while True:
                print("\n1. Show grades")
                print("2. List personal information")
                print("Q. Go back")
                student_choice = input("What do you want to do? ")
                if student_choice == "1":
                    grades = selected_student["grades"]
                    for course, grade in grades.items():
                        print(course, grade)
                elif student_choice == "2":
                        print("\nName:", selected_student["name"]) 
                        print("Student-ID:", selected_student["student_id"]) 
                        print("Email:", selected_student["email"]) 
                        print("Age:", selected_student["age"])
                elif student_choice.lower().strip() == "q":
                    break
                else:
                    print("Invalid choice. Please try again.\n")

def add_student(students: list[dict]):
        """
        Adds a student to the list
        
        Args:
            students (list[dict]): list of all students
        """
        new_students = {}
        while True:
            add_student_name = input("Name: ")
            if len(add_student_name) < 2:
                print("The name is too short. Please try again.")
            elif len(add_student_name) > 60:
                print("The name is too long. Please try again.")
            elif add_student_name.replace(" ", "").isalpha():
                new_students["name"] = add_student_name
                break
            else:
                print("No numbers or special characters allowed. Please try again.")

        while True:
            add_student_id = input("Student-ID: ")
            if add_student_id.isdigit():
                new_students["student_id"] = add_student_id 
                break
            else:
                print("Student-ID can only be numbers. Please try again.")
        students.append(new_students)
        print("Student added!")

def remove_student(students: list[dict]):
    """
    Removes a student
    
    Args:
        students (list[dict]): list of all students
    """
    while True:
        student_to_remove = input("Enter the name of the student you want to remove: ")
        for index, student in enumerate(students):
            if student["name"] == student_to_remove:
                del students[index]
                print("Student removed!")
                break
        else:
            print("There is no student with that name. Please try again.")
        break

while True:
    print("\nWelcome to the student portal!\n")
    print("1. List all students")
    print("2. Add a student")
    print("3. Remove a student")
    print("Q. Exit\n")
    users_choice = input("What do you want to do? ")

    if users_choice == "1":
        print()
        list_students_menu(students=students)
    elif users_choice == "2":
        add_student(students=students)
    elif users_choice == "3":
        remove_student(students=students)
    elif users_choice.lower().strip() == "q":
        break
    else:
        print("Invalid choice. Please try again.")