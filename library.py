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

    def view_books(self):
        if not self.books:
            print("There are no books in the library yet.")
            return
        else:
            print("\nList of Books:")
            print("+----------------------+-------------------------+---------------+------------+")
            print("| Title                | Authors                 | ISBN          | Year       |")
            print("+----------------------+-------------------------+---------------+------------+")

            for book in self.books:

                if len(book.title) > 20:
                    title = (book.title[:20] + '...')
                else:
                    title = book.title.ljust(20)
                
                if len(", ".join(book.authors)) > 23:
                    authors = (", ".join(book.authors)[:23] + '...') 
                else:
                    authors = ", ".join(book.authors).ljust(23)

                isbn = book.isbn.ljust(13)
                year = str(book.publishing_year).ljust(10)

                print(f"| {title} | {authors} | {isbn} | {year} |")
                print("+----------------------+-------------------------+---------------+------------+")
            # for book in self.books:
            #     print(book)
    
    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                self.books = [Book.from_dict(book) for book in json.load(file)]
        except FileNotFoundError:
            self.books = []