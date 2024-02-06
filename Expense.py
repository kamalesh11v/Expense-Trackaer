import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Create expenses table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   item TEXT NOT NULL,
                   amount REAL NOT NULL,
                   date TEXT NOT NULL)''')
conn.commit()

def add_expense(item, amount, date):
    """Add a new expense to the database."""
    cursor.execute("INSERT INTO expenses (item, amount, date) VALUES (?, ?, ?)", (item, amount, date))
    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    """View all expenses stored in the database."""
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    if not expenses:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(f"ID: {expense[0]}, Item: {expense[1]}, Amount: {expense[2]}, Date: {expense[3]}")

def calculate_total_expenses():
    """Calculate the total amount of expenses."""
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = cursor.fetchone()[0]
    if total_expenses:
        print(f"Total expenses: {total_expenses}")
    else:
        print("No expenses recorded yet.")

# Example usage
add_expense("Groceries", 50.00, "2024-02-06")
add_expense("Gas", 30.00, "2024-02-05")
add_expense("Dinner", 40.00, "2024-02-04")

print("\n--- All Expenses ---")
view_expenses()

print("\n--- Total Expenses ---")
calculate_total_expenses()

# Close connection to SQLite database
conn.close()
