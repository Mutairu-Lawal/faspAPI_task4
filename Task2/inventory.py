import json
import os
import math

BOOKS_FILE = "books.json"


class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = round(float(price), 2)
        self.stock = int(stock)

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["price"], data["stock"])


def load_inventory():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            data = json.load(f)
            return [Book.from_dict(b) for b in data]
    return []


def save_inventory(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump([b.to_dict() for b in books], f, indent=4)
