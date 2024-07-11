import json
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def save_books(self, filename='books.json'):
        with open(filename, 'w')as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)