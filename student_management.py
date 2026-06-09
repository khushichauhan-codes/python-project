def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{course}\n")

    print("✅ Student Added Successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No Students Found!\n")
                return

            print("\n===== STUDENT RECORDS =====")

            for line in data:
                name, roll, course = line.strip().split(",")

                print(f"Name   : {name}")
                print(f"Roll No: {roll}")
                print(f"Course : {course}")
                print("--------------------------")

    except FileNotFoundError:
        print("No Student Records Found!\n")


def search_student():
    roll_search = input("Enter Roll Number to Search: ")

    try:
        with open("students.txt", "r") as file:
            found = False

            for line in file:
                name, roll, course = line.strip().split(",")

                if roll == roll_search:
                    print("\n🎯 Student Found!")
                    print("Name   :", name)
                    print("Roll No:", roll)
                    print("Course :", course)

                    found = True
                    break

            if not found:
                print("❌ Student Not Found!")

    except FileNotFoundError:
        print("No Student Records Found!")


def delete_student():
    roll_delete = input("Enter Roll Number to Delete: ")

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            found = False

            for line in lines:
                name, roll, course = line.strip().split(",")

                if roll != roll_delete:
                    file.write(line)
                else:
                    found = True

        if found:
            print("🗑️ Student Deleted Successfully!")
        else:
            print("❌ Student Not Found!")

    except FileNotFoundError:
        print("No Student Records Found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("👋 Thank You!")
        break

    else:
        print("❌ Invalid Choice!")
