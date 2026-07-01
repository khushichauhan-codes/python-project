def add_movie():
    name = input("Enter Movie Name: ")
    year = input("Enter Release Year: ")

    with open("movies.txt", "a") as file:
        file.write(f"{name},{year}\n")

    print("Movie Added Successfully!")


def view_movies():
    try:
        with open("movies.txt", "r") as file:
            movies = file.readlines()

            if not movies:
                print("No Movies Found!")
                return

            print("\n===== MOVIE COLLECTION =====")

            for movie in movies:
                name, year = movie.strip().split(",")

                print("Movie :", name)
                print("Year  :", year)
                print("------------------------")

    except FileNotFoundError:
        print("No Movie Collection Found!")


while True:

    print("\n===== MOVIE COLLECTION MANAGER =====")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_movie()

    elif choice == "2":
        view_movies()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")