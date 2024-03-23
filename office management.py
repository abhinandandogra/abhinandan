def add_employee(employees, name, employee_id, department):
    employees.append({'name': name, 'employee_id': employee_id, 'department': department})
    print("Employee added successfully.")

def view_all_employees(employees):
    if employees:
        idx = 1
        for employee in employees:
            print(f"{idx}. Name: {employee['name']}, ID: {employee['employee_id']}, Department: {employee['department']}")
            idx += 1
    else:
        print("No employees available.")

def search_employee(employees, name):
    found_employees = [employee for employee in employees if employee['name'].lower() == name.lower()]
    if found_employees:
        for employee in found_employees:
            print(f"Name: {employee['name']}, ID: {employee['employee_id']}, Department: {employee['department']}")
    else:
        print("Employee not found.")

def remove_employee(employees, employee_id):
    for employee in employees:
        if employee['employee_id'] == employee_id:
            employees.remove(employee)
            print("Employee removed successfully.")
            return
    print("Employee not found.")

def main():
    employees = []
    while True:
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

