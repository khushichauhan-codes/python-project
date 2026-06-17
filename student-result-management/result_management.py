def add_result():
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    with open("results.txt", "a") as file:
        file.write(f"{name},{marks}\n")

    print("Result Added Successfully!")


def view_results():
    try:
        with open("results.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No Records Found!")
                return

            print("\n===== RESULTS =====")

            for record in data:
                name, marks = record.strip().split(",")

                if float(marks) >= 40:
                    status = "PASS"
                else:
                    status = "FAIL"

                print(f"Name: {name}")
                print(f"Marks: {marks}")
                print(f"Status: {status}")
                print("----------------")

    except FileNotFoundError:
        print("No Records Found!")


while True:

    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_result()

    elif choice == "2":
        view_results()

    elif choice == "3":
        break

    else:
        print("Invalid Choice!")