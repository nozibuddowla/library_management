from library import Library
from book import Book

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Exit")

def add_books(library):
    title = input("Enter title: ").strip()
    authors = input("Enter authors (comma-separated): ").strip().split(',')
    isbn = input("Enter ISBN: ").strip()
    year = int(input("Enter publishing year: ").strip())
    price = float(input("Enter price: ").strip())
    quantity = int(input("Enter quantity: ").strip())
    book = Book(title, authors, isbn, year, price, quantity)
    library.add_book(book)
    print("Book added successfully!")

def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                add_books(library)
            case '2':
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()