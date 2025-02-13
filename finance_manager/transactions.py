class Transaction:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"R$ {self.amount:.2f} in {self.category}"