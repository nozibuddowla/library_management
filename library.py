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

    def save_lend_log(self, filename='lend_log.json'):
        with open(filename, 'w') as file:
            json.dump(self.lend_log, file)

    def display_books(self, books):
        print("\nList of Books:")
        print("+----+----------------------+-------------------------+---------------+-------------+")
        print("| No | Title                | Authors                 | ISBN          | Quantity    |")
        print("+----+----------------------+-------------------------+---------------+-------------+")
        for i, book in enumerate(books):
            title = book.title[:20].ljust(20)
            authors = ", ".join(book.authors)[:23].ljust(23)
            isbn = book.isbn.rjust(13)
            quantity = str(book.quantity).ljust(11)
            print(f"| {str(i+1).ljust(2)} | {title} | {authors} | {isbn} | {quantity} |")
            print("+----+----------------------+-------------------------+---------------+-------------+")

    def view_books(self):
        if not self.books:
            print("There are no books in the library.")
            return
        else:
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
            if any(search_term.lower() in author.lower() for author in book.authors):
                results.append(book)
        return results
    
    def remove_book(self, book):
        self.books.remove(book)
        self.save_books()

    def load_books(self, filename='books.json'):
        try:
            with open(filename, 'r') as file:
                self.books = [Book.from_dict(book) for book in json.load(file)]
        except FileNotFoundError:
            self.books = []

    def load_lend_log(self, filename='lend_log.json'):
        try:
            with open(filename, 'r') as file:
                self.lend_log = json.load(file)
        except FileNotFoundError:
            self.lend_log = []

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
                        self.save_lend_log()
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
            print("\nList of Lent Books:")
            print("+----+----------------------+-------------------------+---------------+-------------------------+")
            print("| No | Title                | Authors                 | ISBN          | Borrower                |")
            print("+----+----------------------+-------------------------+---------------+-------------------------+")
            for i, log in enumerate(self.lend_log):
                title = log['title'][:20].ljust(20)
                authors = ", ".join(log['authors'])[:23].ljust(23)
                isbn = log['isbn'].rjust(13)
                borrower = log['borrower'][:23].ljust(23)
                print(f"| {str(i+1).ljust(2)} | {title} | {authors} | {isbn} | {borrower} |")
                print("+----+----------------------+-------------------------+---------------+-------------------------+")

    def return_book(self, search_term):
        matching_lent_books = [log for log in self.lend_log if search_term.lower() in log['title'].lower() or search_term in log['isbn']]
        if matching_lent_books:
            print(f"\nReturn Book Search Results for '{search_term}':")
            print("+----+----------------------+-------------------------+---------------+---------------------+")
            print("| No | Title                | Authors                 | ISBN          | Borrower            |")
            print("+----+----------------------+-------------------------+---------------+---------------------+")
            for i, log in enumerate(matching_lent_books):
                title = log['title'][:20].ljust(20)
                authors = ", ".join(log['authors'])[:23].ljust(23)
                isbn = log['isbn'].rjust(13)
                borrower = log['borrower'][:20].ljust(20)
                print(f"| {str(i+1).ljust(2)} | {title} | {authors} | {isbn} | {borrower} |")
                print("+----+----------------------+-------------------------+---------------+---------------------+")
            try:
                book_index = int(input("Enter the number of the book you want to return: ").strip()) - 1
                if 0 <= book_index < len(matching_lent_books):
                    selected_book = matching_lent_books[book_index]
                    for book in self.books:
                        if book.isbn == selected_book['isbn']:
                            book.quantity += 1
                            self.lend_log.remove(selected_book)
                            self.save_books()
                            self.save_lend_log()
                            print(f"Book '{book.title}' returned successfully! Current quantity: {book.quantity}")
                            break
                        else:
                            print("The book is not found in the library, adding it back.")
                            returned_book = Book.from_dict(selected_book)
                            returned_book.quantity = 1
                            self.books.append(returned_book)
                            self.lend_log.remove(selected_book)
                            self.save_books()
                            self.save_lend_log()
                            print(f"Book '{returned_book.title}' returned successfully!")
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print(f"No lent books found matching '{search_term}'.")