import os
import json
from transaction import Transaction
from budget_utils import group_by_category, calculate_totals

DATA_FILE = "data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Transaction.from_dict(tx) for tx in data]
    return []


def save_data(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump([tx.to_dict() for tx in transactions], f, indent=4)


def add_transaction(transactions):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., food, rent): ")
    amount = float(input("Enter amount: "))
    tx = Transaction(date, category, amount)
    transactions.append(tx)
    print("Transaction added!")


def view_summary(transactions):
    grouped = group_by_category(transactions)
    totals = calculate_totals(grouped)
    if not totals:
        print("No transactions yet.")
        return
    print("\n--- Expense Summary ---")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")


def main():
    transactions = load_data()
    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction(transactions)
            save_data(transactions)
        elif choice == "2":
            view_summary(transactions)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
