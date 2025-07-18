from datetime import datetime


class Transaction:
    def __init__(self, date, category, amount):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.category = category
        self.amount = float(amount)

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "category": self.category,
            "amount": self.amount
        }

    @staticmethod
    def from_dict(data):
        return Transaction(data["date"], data["category"], data["amount"])
