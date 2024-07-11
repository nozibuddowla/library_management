from library import Library
from book import Book

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search books")
    print("4. Exit")

def add_books(library):
    title = input("Enter title: ").strip()
    authors = input("Enter authors (comma-separated): ").strip().split(',')
    isbn = input("Enter ISBN: ").strip()
    year = input("Enter publishing year: ").strip()
    price = float(input("Enter price: ").strip())
    quantity = int(input("Enter quantity: ").strip())
    book = Book(title, authors, isbn, year, price, quantity)
    library.add_book(book)
    print("Book added successfully!")

def search_books(library):
    search_term = input('Enter Book title or ISBN to search: ').strip()
    results = library.search_books(search_term)
    if results:
        print(f"\nSearch Results for '{search_term}':")
        library.display_books(results)
    else:
        print(f"No books found matching '{search_term}'.")

def main():
    library = Library()
    library.load_books()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                add_books(library)
            case '2':
                library.view_books()
            case '3':
                search_books(library)
            case '4':
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()