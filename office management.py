def main():
    employees = []
    for _ in range(100):  # Choose a suitable upper limit for the number of iterations
        print("\n======= Office Management System =======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Remove Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            department = input("Enter employee department: ")
            add_employee(employees, name, employee_id, department)

        elif choice == '2':
            view_all_employees(employees)

        elif choice == '3':
            name = input("Enter employee name to search: ")
            search_employee(employees, name)

        elif choice == '4':
            employee_id = input("Enter employee ID to remove: ")
            remove_employee(employees, employee_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the program by calling the main function
main()
