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
            json.dump([book.to_dict() for book in self.books], file)

    def view_books(self):
        if not self.books:
            print("There are no books in the library yet.")
            return
        else:
            print("\nList of Books:")
            self.display_books(self.books)
    
    def search_books(self, search_term):
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term in book.isbn:
                results.append(book)
        return results
    
    def search_books_by_author(self, search_term):
        results = []
        for book in self.books:
            if search_term.lower() in book.authors.lower():
                results.append(book)
        return results
    
    def search_books_by_author(self, search_term):
        results = []
        for book in self.books:
            for author in book.authors:
                if search_term.lower() in author.lower():
                    results.append(book)
        return results
    
    def display_books(self, books):
        print("+----------------------+-------------------------+----------------+------------+")
        print("| Title                | Authors                 | ISBN           | Year       |")
        print("+----------------------+-------------------------+----------------+------------+")

        for book in books:
            if len(book.title) > 20:
                title = (book.title[:20] + '...')
            else:
                title = book.title.ljust(20)
                
            if len(", ".join(book.authors)) > 23:
                authors = (", ".join(book.authors)[:23] + '...') 
            else:
                authors = ", ".join(book.authors).ljust(23)

            isbn = book.isbn.rjust(13)
            year = str(book.publishing_year).ljust(10)

            print(f"| {title} | {authors} | {isbn} | {year} |")
            print("+----------------------+-------------------------+----------------+------------+")
    
    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                self.books = [Book.from_dict(book) for book in json.load(file)]
        except FileNotFoundError:
            self.books = []