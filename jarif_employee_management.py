def data(name, emp_id, salary):
    formatted = f"{name} | {emp_id} | {salary}"
    return formatted


def add_employee(name, emp_id, salary):
    line = data(name, emp_id, salary)

    file = open("employees.txt", "a")
    file.write(line + "\n")
    file.close()

    return True


def view_employees():
    file = open("employees.txt", "r")
    content = file.read()
    file.close()

    print("\n--- Employees List ---")
    print(content)
    print("----------------------")


while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("\nChoose Option: ")

    if choice == "1":
        name = input("Enter Name: ")
        emp_id = input("Enter ID: ")
        salary = input("Enter Salary: ")

        saved = add_employee(name, emp_id, salary)

        if saved:
            print("\nEmployee Added Successfully")

    elif choice == "2":
        view_employees()

    elif choice == "3":
        print("Exit")
        break

    else:
        print("Invalid Option")