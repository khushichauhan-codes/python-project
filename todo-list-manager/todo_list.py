def add_task():
    task = input("Enter Task: ")

    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("✅ Task Added Successfully!")


def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("No Tasks Found!")
                return

            print("\n===== TASK LIST =====")

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

    except FileNotFoundError:
        print("No Tasks Available!")


def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No Tasks Found!")
            return

        view_tasks()

        task_num = int(input("\nEnter Task Number to Delete: "))

        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            print("✅ Task Deleted Successfully!")

        else:
            print("❌ Invalid Task Number!")

    except:
        print("❌ Error!")


while True:

    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("👋 Thank You!")
        break

    else:
        print("❌ Invalid Choice!")