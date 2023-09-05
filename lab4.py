employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
]

def search_employee_data():
    while True:
        print("Arpit Panwar")
        print("E22CSEU1105")
        print("Search Options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary (>, <, <=, >=)")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            age = int(input("Enter the age to search for: "))
            results = [employee for employee in employee_data if employee["Age"] == age]
        elif choice == "2":
            name = input("Enter the name to search for: ")
            results = [employee for employee in employee_data if employee["Name"].lower() == name.lower()]
        elif choice == "3":
            operator = input("Enter the operator (> or < or <= or >=): ")
            salary = int(input("Enter the salary to search for: "))
            
            if operator == ">":
                results = [employee for employee in employee_data if employee["Salary (PM)"] > salary]
            elif operator == "<":
                results = [employee for employee in employee_data if employee["Salary (PM)"] < salary]
            elif operator == ">=":
                results = [employee for employee in employee_data if employee["Salary (PM)"] >= salary]
            elif operator == "<=":
                results = [employee for employee in employee_data if employee["Salary (PM)"] <= salary]
            else:
                print("Invalid operator. Please use >, <, <=, or >=.")
                continue
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue
        
        if not results:
            print("No matching records found.")
        else:
            print("Matching Employee Data:")
            for employee in results:
                print(f"Employee ID: {employee['Employee ID']}")
                print(f"Name: {employee['Name']}")
                print(f"Age: {employee['Age']}")
                print(f"Salary (PM): {employee['Salary (PM)']}")
                print()

if __name__ == "__main__":
    search_employee_data()