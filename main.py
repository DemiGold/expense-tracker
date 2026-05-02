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
    try:
        with open("expense.csv","r") as f:
            pass
    except FileNotFoundError:
        with open("expense.csv","w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount"])
    
    while True:
        category = input("Enter category (e.g. Food, Transport):").strip()
        if category:
            break
        else:
            print("Input required...Category cannot be empty.")

    while True:
        try:
            amount = float(input("Enter expense amount: ₦"))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.\n")

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
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        break
    else:
        print("Invalid input... Choose from 1-7")