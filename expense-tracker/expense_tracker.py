def add_expense():
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: ₹"))

    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount}\n")

    print("✅ Expense Added Successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No Expenses Found!")
                return

            total = 0

            print("\n===== EXPENSES =====")

            for line in data:
                category, amount = line.strip().split(",")

                print(f"Category : {category}")
                print(f"Amount   : ₹{amount}")
                print("---------------------")

                total += float(amount)

            print(f"\n💰 Total Spending: ₹{total}")

    except FileNotFoundError:
        print("No Expense Records Found!")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("👋 Thank You!")
        break

    else:
        print("❌ Invalid Choice!")
