import json
from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.lend_log = []

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def save_books(self, filename='books.json'):
        with open(filename, 'w')as file:
            json.dump([book.to_dict() for book in self.books], file)

    def view_books(self):
        if not self.books:
            print("There are no books in the library.")
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
    
    def remove_book(self, book):
        self.books.remove(book)
        self.save_books()
    
    def display_books(self, books):
        print("+----+----------------------+-------------------------+---------------+-------------+")
        print("| No | Title                | Authors                 | ISBN          | Quantity    |")
        print("+----+----------------------+-------------------------+---------------+-------------+")
        for i, book in enumerate(books):
            if len(book.title) > 20:
                title = (book.title[:20])
            else:
                title = book.title.ljust(20)
                
            if len(", ".join(book.authors)) > 23:
                authors = (", ".join(book.authors)[:23]) 
            else:
                authors = ", ".join(book.authors).ljust(23)

            isbn = book.isbn.rjust(13)
            quantity = str(book.quantity).ljust(11)

            print(f"| {str(i+1).ljust(2)} | {title} | {authors} | {isbn} | {quantity} |")
            print("+----+----------------------+-------------------------+---------------+-------------+")

    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                self.books = [Book.from_dict(book) for book in json.load(file)]
        except FileNotFoundError:
            self.books = []

    def lend_book(self, search_term):
        results = self.search_books(search_term)
        if results:
            print(f"\nSearch Results for '{search_term}':")
            self.display_books(results)
            try:
                book_index = int(input("Enter the number of the book you want to lend: ").strip()) - 1
                if 0 <= book_index < len(results):
                    book_to_lend = results[book_index]
                    if book_to_lend.quantity > 0:
                        borrower_name = input("Enter your name for borrowing the book: ").strip()
                        book_to_lend.quantity -= 1
                        self.save_books()
                        self.lend_log.append({
                            "title": book_to_lend.title,
                            "authors": book_to_lend.authors,
                            "isbn": book_to_lend.isbn,
                            "borrower": borrower_name
                        })
                        print(f"Book '{book_to_lend.title}' lent successfully! Remaining quantity: {book_to_lend.quantity}")
                    else:
                        print("Not enough books available to lend.")
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print(f"No books found matching '{search_term}'.")

    def view_lent_books(self):
        if not self.lend_log:
            print('No books have been let out.')
        else:
            print(self.lend_log)
            print("\nList of Lent Books:")
            print("+----+----------------------+-------------------------+---------------+-------------------------+")
            print("| No | Title                | Authors                 | ISBN          | Borrower                |")
            print("+----+----------------------+-------------------------+---------------+-------------------------+")
            for i, log in enumerate(self.lend_log):
                title = log['title'].ljust(20)[:20]
                authors = ','.join(log['authors']).ljust(23)[:23]
                isbn = log["isbn"].rjust(13)
                borrower = log["borrower"].ljust(23)[:23]

                print(f"| {str(i+1).ljust(2)} | {title} | {authors} | {isbn} | {borrower} |")
                print("+----+----------------------+-------------------------+---------------+-------------------------+")