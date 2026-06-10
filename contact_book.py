def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")

    print("✅ Contact Added Successfully!")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No Contacts Found!")
                return

            print("\n===== CONTACT LIST =====")

            for line in data:
                name, phone = line.strip().split(",")
                print(f"Name : {name}")
                print(f"Phone: {phone}")
                print("--------------------")

    except FileNotFoundError:
        print("No Contacts Found!")


def search_contact():
    search_name = input("Enter Name to Search: ")

    try:
        with open("contacts.txt", "r") as file:
            found = False

            for line in file:
                name, phone = line.strip().split(",")

                if name.lower() == search_name.lower():
                    print("\n📞 Contact Found!")
                    print("Name :", name)
                    print("Phone:", phone)
                    found = True
                    break

            if not found:
                print("Contact Not Found!")

    except FileNotFoundError:
        print("No Contacts Found!")


def delete_contact():
    delete_name = input("Enter Name to Delete: ")

    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()

        with open("contacts.txt", "w") as file:
            found = False

            for line in lines:
                name, phone = line.strip().split(",")

                if name.lower() != delete_name.lower():
                    file.write(line)
                else:
                    found = True

        if found:
            print("🗑️ Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    except FileNotFoundError:
        print("No Contacts Found!")


while True:
    print("\n===== CONTACT BOOK SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
