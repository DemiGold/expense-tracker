# Expense Tracker CLI

A command-line personal expense tracker built with Python as part of my ML Engineering learning journey. This is the final project for Phase 1 of my roadmap, covering Python fundamentals, OOP, file handling, and error handling.

## How It Works

When you run the program, a menu appears with 6 options. You can add expenses which are automatically saved to a CSV file with the date, category, and amount. All data persists between sessions — closing the program does not delete your records. The program validates every input and handles missing files gracefully without crashing.

## Features

- Add expenses with category, amount, and auto-generated date
- View all saved expenses
- View total number of expenses and total amount spent
- Filter expenses by category with a category total
- Find the single highest expense across all records
- Delete all expenses with a confirmation prompt

## Tech Stack

- Python 3
- CSV file handling
- Object-Oriented Programming
- datetime module

## Project Structure
expense-tracker/
├── main.py       # Menu loop, user interaction, and all options
├── models.py     # Expense class with str and to_row() methods
├── expense.csv   # Persistent data storage
└── README.md     # Project documentation

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DemiGold/expense-tracker.git
   ```

2. **Navigate into the folder:**
   ```bash
   cd expense-tracker
   ```

3. **Run the program:**
   ```bash
   python main.py
   ```

## What I Learned

- Designing and using Python classes with OOP
- Reading and writing CSV files with the csv and DictReader modules
- Handling errors gracefully with try/except across all user inputs
- Structuring a Python project across multiple files using imports
- Using Git and GitHub for version control across two machines
  
## Author

**DemiGold** — Aspiring ML Engineer  
[github.com/DemiGold](https://github.com/DemiGold)  
University of Lagos — BSc Mathematics and Computer Science
