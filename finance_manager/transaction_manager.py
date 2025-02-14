from finance_manager.transaction import Transaction
from finance_manager.file_handler import save_transactions, load_transactions


class TransactionManager:

    def __init__(self):
        self._transactions = []

    def add_transaction(self, amount, category):
        self._transactions.append(Transaction(amount, category))
        print("✅ Transaction added successfully!\n")

    def __str__(self):
        if not self._transactions:
            return "📂 No transactions recorded yet."

        return "\n📜 Your transactions:\n" + "\n".join(str(t) for t in self._transactions)

    def check_balance(self):
        total_balance = sum(t.get_amount() for t in self._transactions)
        print(f"💰 Total Balance: R$ {total_balance:.2f}")

    def save_to_file(self):
        save_transactions(self._transactions)

    def load_from_file(self, filename):
        self._transactions = load_transactions(filename)