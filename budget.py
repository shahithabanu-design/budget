import datetime

# Initialize expense data and salary
expense_data = {
    'expenses': [],
    'budget': {'Food': 0, 'Entertainment': 0, 'Utilities': 0, 'Other': 0},
    'savings': 0,
    'salary': 0
}

# Function to input salary
def set_salary(amount):
    expense_data['salary'] = amount
    print(f"Salary set to {amount}.")

# Function to set monthly budget
def set_budget(category, amount):
    if category not in expense_data['budget']:
        print("Invalid category!")
        return
    expense_data['budget'][category] = amount
    print(f"Budget for '{category}' set to {amount}.")

# Function to log an expense
def log_expense(category, amount, description):
    if category not in expense_data['budget']:
        print("Invalid category!")
        return
    expense = {
        'category': category,
        'amount': amount,
        'description': description,
        'date': str(datetime.date.today())
    }
    expense_data['expenses'].append(expense)
    print(f"Expense of {amount} logged under '{category}'.")

# Function to log savings
def log_savings(amount):
    expense_data['savings'] += amount
    print(f"Savings of {amount} logged.")

# Function to calculate and suggest spending limits
def calculate_spending_limits():
    salary = expense_data['salary']
    suggested_savings = salary * 0.10  # 10% of salary for savings
    remaining_salary = salary - suggested_savings  # 90% remaining for spending

    print(f"\nSuggested Savings (10% of salary): {suggested_savings}")
    print(f"Remaining for Spending: {remaining_salary}")

    num_categories = len(expense_data['budget'])
    suggested_per_category = remaining_salary / num_categories  # Equal spending suggestion for each category

    print(f"\nSuggested spending for each category (to ensure savings):")
    for category in expense_data['budget']:
        print(f"{category}: {suggested_per_category:.2f}")
    
    return suggested_savings, remaining_salary

# Function to generate spending and savings report
def generate_report():
    print("\n--- Spending and Savings Report ---")
    total_spent = {'Food': 0, 'Entertainment': 0, 'Utilities': 0, 'Other': 0}
    total_expenses = 0

    for expense in expense_data['expenses']:
        total_spent[expense['category']] += expense['amount']

    # Calculate total expenses
    total_expenses = sum(total_spent.values())

    # Check if the total expenses and savings exceed the salary
    total_needed = total_expenses + expense_data['savings']

    print(f"\nTotal Expenses: {total_expenses}")
    print(f"Total Savings: {expense_data['savings']}")
    print(f"Total Needed (Expenses + Savings): {total_needed}")
    print(f"Salary: {expense_data['salary']}")

    if total_needed > expense_data['salary']:
        print("\nWarning: Your expenses and savings exceed your salary. You may need to adjust your budget.")
    else:
        print("Your expenses and savings are within your salary.")

    # Display expenses in each category
    for category in expense_data['budget']:
        spent = total_spent[category]
        budget = expense_data['budget'][category]
        print(f"{category}: Spent = {spent} | Budget = {budget}")
        if spent > budget:
            print(f"Alert! You have exceeded your {category} budget by {spent - budget}.")
    
# Function to view expense history
def view_history():
    print("\n--- Expense History ---")
    for expense in expense_data['expenses']:
        print(f"{expense['date']} | {expense['category']} | {expense['description']} | Amount: {expense['amount']}")

# Main function to interact with the user
def expense_tracker():
    print("Welcome to the Expense Tracker!")
    
    while True:
        print("\n1. Set Salary")
        print("2. Set Budget")
        print("3. Log Expense")
        print("4. Log Savings")
        print("5. Generate Report")
        print("6. View Expense History")
        print("7. Calculate Spending Limits (Suggested)")
        print("8. Exit")
        
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            salary = float(input("Enter your monthly salary: "))
            set_salary(salary)
        elif choice == '2':
            category = input("Enter category to set budget (Food, Entertainment, Utilities, Other): ").capitalize()
            amount = float(input("Enter budget amount: "))
            set_budget(category, amount)
        elif choice == '3':
            category = input("Enter category (Food, Entertainment, Utilities, Other): ").capitalize()
            amount = float(input("Enter expense amount: "))
            description = input("Enter a brief description of the expense: ")
            log_expense(category, amount, description)
        elif choice == '4':
            savings = float(input("Enter amount to save: "))
            log_savings(savings)
        elif choice == '5':
            generate_report()
        elif choice == '6':
            view_history()
        elif choice == '7':
            calculate_spending_limits()
        elif choice == '8':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the expense tracker
expense_tracker()
