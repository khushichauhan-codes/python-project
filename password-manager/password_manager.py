def save_password():
    website = input("Enter Website Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{website},{username},{password}\n")

    print("✅ Password Saved Successfully!")


def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No Passwords Saved!")
                return

            print("\n===== SAVED PASSWORDS =====")

            for record in data:
                website, username, password = record.strip().split(",")

                print(f"Website : {website}")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print("---------------------------")

    except FileNotFoundError:
        print("No Password Records Found!")


while True:

    print("\n===== PASSWORD MANAGER =====")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        save_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("👋 Thank You!")
        break

    else:
        print("❌ Invalid Choice!")