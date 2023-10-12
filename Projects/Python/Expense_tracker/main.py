class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def view_expenses(self):
        if self.expenses:
            for category, amount in self.expenses.items():
                print(f"{category}: ${amount:.2f}")
        else:
            print("No expenses recorded yet.")

    def total_expenses(self):
        return sum(self.expenses.values())

if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: $"))
            tracker.add_expense(category, amount)
            print("Expense added successfully.")

        elif choice == "2":
            print("\n--- Expenses ---")
            tracker.view_expenses()

        elif choice == "3":
            total = tracker.total_expenses()
            print(f"\nTotal Expenses: ${total:.2f}")

        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
