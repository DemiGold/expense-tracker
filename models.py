class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.category}: ₦{self.amount}"
    
    def to_row(self):
        return [self.date, self.category, self.amount]