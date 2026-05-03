from models import Expense
from datetime import datetime
import csv

def show_menu():
    print("===== Main Menu =====")
    print("1. Add an expense")
    print("2. View all expense")
    print("3. View total spent")
    print("4. Filter by category")
    print("5. Show highest expense")
    print("6. Delete all expense")
    print("7. Quit")
    print("="*22)

def add_expense():
    current_time = datetime.now()

    # create header if file doesn't exist yet
    try:
        with open("expense.csv","r") as f:
            pass
    except FileNotFoundError:
        with open("expense.csv","w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount"])
    
    # keep asking until category isn't empty
    while True:
        category = input("Enter category (e.g. Food, Transport):").strip().capitalize()
        if category:
            break
        else:
            print("Input required...Category cannot be empty.")

    # keep asking until a valid number is entered
    while True:
        try:
            amount = float(input("Enter expense amount: ₦"))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.\n")

    # create Expense object and save to CSV
    date = current_time.strftime("%Y-%m-%d")
    new_expense = Expense(date, category, amount)
    with open("expense.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_expense.to_row())

while True:
    show_menu()
    choice = input("Enter option: ")

    if choice == "1":
        add_expense()
        print("Expense added successfully!\n")

    elif choice == "2":
        # load and display all expenses using __str__
        try:
            with open("expense.csv","r",newline="") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    print(Expense(row[0], row[1], row[2]))
                print()
        except FileNotFoundError:
            print("No Expense recorded yet!")

    elif choice == "3":
        total_spent = 0.0
        try:
            with open("expense.csv","r",newline="") as f:
                reader = csv.reader(f)
                next(reader)
                data = list(reader)
                row_count = len(data)
                for row in data:
                    total_spent += float(row[2])
                print(f"Total Expense: {row_count} | Total Spent: ₦{total_spent}\n")
        except FileNotFoundError:
            print("No Expense recorded yet!")

    elif choice == "4":
        # filter rows matching the entered category
        target_category = input("Enter Category: ").strip().capitalize()
        category_total = 0.0
        try:
            with open('expense.csv', 'r', newline='') as infile:
                reader = csv.DictReader(infile)
                print(f"\n--- Expenses for Category: {target_category} ---")
                found = False
                for row in reader:
                    if row['Category'] == target_category:
                        amount = float(row['Amount'])
                        print(f"Date: {row['Date']}, Amount: ₦{amount}")
                        category_total += amount
                        found = True
                if found:
                    print("-" * 30)
                    print(f"Total for {target_category}: ₦{category_total}")
                else:
                    print(f"No expenses found in category: {target_category}")
                print()
        except FileNotFoundError:
            print("No Expense recorded yet!\n")

    elif choice == "5":
        # track highest amount by comparing each row
        highest_expense = None
        try:
            with open("expense.csv", "r", newline="") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    current_expense = Expense(row[0], row[1], float(row[2]))
                    if highest_expense is None or current_expense.amount > highest_expense.amount:
                        highest_expense = current_expense
                if highest_expense:
                    print(f"\n--- Highest Expense ---")
                    print(f"Date: {highest_expense.date}")
                    print(f"Category: {highest_expense.category}")
                    print(f"Amount: ₦{highest_expense.amount}\n")
                else:
                    print("No expenses recorded yet!\n")
        except FileNotFoundError:
            print("No Expense recorded yet!\n")

    elif choice == "6":
        # overwrite file with just the header to clear all data
        confirm = input("Are you sure you want to delete all expenses? (yes/no): ").lower()
        if confirm == "yes":
            try:
                with open("expense.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Date", "Category", "Amount"])
                print("All expenses deleted successfully!\n")
            except Exception as e:
                print(f"An error occurred: {e}\n")
        else:
            print("Action cancelled.\n")

    elif choice == "7":
        break

    else:
        print("Invalid input... Choose from 1-7")