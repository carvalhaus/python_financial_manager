class Transaction:
    def __init__(self, amount, category):
        self._amount = amount
        self._category = category

    def __str__(self):
        return f"R$ {self._amount:.2f} in {self._category}"

    def get_amount(self):
        return self._amount

    def get_category(self):
        return self._category