import datetime

expenses = {}

while True:
    print("\nEXPENSE TRACKER:")
    print("1. Add Expense")
    print("2. View Spending Pattern")
    print("0. Exit")

    choice = input("Enter your choice (0-2): ")

    if choice == '1':
        date = input("Enter the date (YYYY-MM-DD): ")
        try:
            expense_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")

        if expense_date not in expenses:
            expenses[expense_date] = []

        expenses[expense_date].append({'description': description, 'amount': amount, 'category': category})
        print("Expense added successfully.")

    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nSpending Pattern:")
            for date, daily_expenses in sorted(expenses.items()):
                total_daily_expense = sum(expense['amount'] for expense in daily_expenses)
                print(f"{date}: Total Expense - ${total_daily_expense:.2f}")

                for expense in daily_expenses:
                    print(f"  - {expense['description']}: ${expense['amount']:.2f} ({expense['category']})")

    elif choice == '0':
        break

    else:
        print("Invalid choice. Please try again.")