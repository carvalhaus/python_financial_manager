from datetime import datetime
import os
from finance_manager.transaction import Transaction

def save_transactions(transactions):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/transactions_{date_str}.txt"

    try:
        with open(filename, "w") as file:
            for t in transactions:
                file.write(f"{t.get_amount()}, {t.get_category()}\n")
        print(f"Transactions saved successfully in {filename}!")
    except Exception as e:
        print(f"Error saving transactions: {e}")

def load_transactions(filename):
    try:
        filepath = os.path.join("data", filename)

        with open(filepath, "r") as file:
            transactions = []
            for line in file:
                amount, category = line.strip().split(", ")
                transactions.append(Transaction(float(amount), category))
        print(f"Transactions loaded successfully from {filename}!")
        return transactions
    except FileNotFoundError:
        print(f"Error: File {filename} not found in 'data' directory.")
        return []
    except Exception as e:
        print(f"Error loading transactions: {e}")
        return []