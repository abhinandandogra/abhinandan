class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

class Office:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully.")

    def view_all_employees(self):
        if self.employees:
            idx = 1
            for employee in self.employees:
                print(f"{idx}. Name: {employee.name}, ID: {employee.employee_id}, Department: {employee.department}")
                idx += 1
        else:
            print("No employees available.")

    def search_employee(self, name):
        found_employees = [employee for employee in self.employees if employee.name.lower() == name.lower()]
        if found_employees:
            for employee in found_employees:
                print(f"Name: {employee.name}, ID: {employee.employee_id}, Department: {employee.department}")
        else:
            print("Employee not found.")

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print("Employee removed successfully.")
                return
        print("Employee not found.")

def office_management(office):
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
        employee = Employee(name, employee_id, department)
        office.add_employee(employee)
        office_management(office)

    elif choice == '2':
        office.view_all_employees()
        office_management(office)

    elif choice == '3':
        name = input("Enter employee name to search: ")
        office.search_employee(name)
        office_management(office)

    elif choice == '4':
        employee_id = input("Enter employee ID to remove: ")
        office.remove_employee(employee_id)
        office_management(office)

    elif choice == '5':
        print("Exiting...")
        return

    else:
        print("Invalid choice. Please try again.")
        office_management(office)

office = Office()
office_management(office)
