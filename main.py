from library import Library
from book import Book

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search books by title or ISBN")
    print("4. Search books by author")
    print("5. Remove a book")
    print("6. Lend a book")
    print("7. View lent books")
    print("8. Return a book")
    print("9. Exit")

def add_books(library):
    title = input("Enter title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    authors = input("Enter authors (comma-separated): ").strip()
    if not authors:
        print("Authors cannot be empty.")
        return
    authors = authors.split(',')

    isbn = input("Enter ISBN: ").strip()
    if not isbn:
        print("ISBN cannot be empty.")
        return

    year = input("Enter publishing year: ").strip()
    if not year:
        print("Publishing year cannot be empty.")
        return

    try:
        price = float(input("Enter price: ").strip())
    except ValueError:
        print("Invalid input. Price should be a floating number.")
        return

    try:
        quantity = int(input("Enter quantity: ").strip())
    except ValueError:
        print("Invalid input. Quantity should be an integer.")
        return
    
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


def search_books_by_author(library):
    search_term = input('Enter Book author name to search: ').strip()
    results = library.search_books_by_author(search_term)
    if results:
        print(f"\nSearch Results for author '{search_term}':")
        library.display_books(results)
    else:
        print(f"No books found matching author '{search_term}'.")

def remove_book(library):
    library.view_books()
    search_term =  input('Enter Book title or ISBN to remove: ').strip()
    results = library.search_books(search_term)
    if results:
        print(f"\nSearch Results for '{search_term}':")
        library.display_books(results)
        try:
            book_index = int(input("Enter the number of the book you want to remove: ").strip()) - 1
            if 0 <= book_index < len(results):
                library.remove_book(results[book_index])
                print("Book removed successfully!")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print(f"No books found matching '{search_term}'.")

def lend_book(library):
    library.view_books()
    search_term = input('Enter Book title or ISBN to lend: ').strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    try:
        library.lend_book(search_term)
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def return_book(library):
    search_term = input('Enter Book title or ISBN to return: ').strip()
    try:
        library.return_book(search_term)
    except ValueError as e:
        print(e)

def main():
    library = Library()
    library.load_books()
    library.load_lend_log()

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
                search_books_by_author(library)
            case '5':
                remove_book(library)
            case '6':
                lend_book(library)
            case '7':
                library.view_lent_books()
            case '8':
                return_book(library)
            case '9':
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()