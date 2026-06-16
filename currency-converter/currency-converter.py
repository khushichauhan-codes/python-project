def inr_to_usd(amount):
    return amount / 83


def usd_to_inr(amount):
    return amount * 83


def inr_to_eur(amount):
    return amount / 90


while True:

    print("\n===== CURRENCY CONVERTER =====")
    print("1. INR to USD")
    print("2. USD to INR")
    print("3. INR to EUR")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        amount = float(input("Enter INR Amount: "))
        print("USD =", round(inr_to_usd(amount), 2))

    elif choice == "2":
        amount = float(input("Enter USD Amount: "))
        print("INR =", round(usd_to_inr(amount), 2))

    elif choice == "3":
        amount = float(input("Enter INR Amount: "))
        print("EUR =", round(inr_to_eur(amount), 2))

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")