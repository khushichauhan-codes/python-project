def add_book():
    book = input("Enter Book Name: ")

    with open("books.txt", "a") as file:
        file.write(book + "\n")

    print("✅ Book Added Successfully!")


def view_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

            if not books:
                print("No Books Available!")
                return

            print("\n📚 Library Books:")

            for book in books:
                print("-", book.strip())

    except FileNotFoundError:
        print("No Books Found!")


def search_book():
    name = input("Enter Book Name: ")

    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

            found = False

            for book in books:
                if name.lower() == book.strip().lower():
                    found = True
                    break

            if found:
                print("✅ Book Found!")
            else:
                print("❌ Book Not Found!")

    except FileNotFoundError:
        print("No Books Found!")


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        print("👋 Thank You!")
        break

    else:
        print("❌ Invalid Choice!")