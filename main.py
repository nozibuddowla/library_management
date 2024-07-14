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

def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if not value and required:
            print("This field cannot be empty.")
        else:
            return value

def get_int_input(prompt):
    while True:
        try:
            return int(get_input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def add_books(library):
    title = get_input("Enter title: ")

    authors = get_input("Enter authors (comma-separated): ").split(',')

    isbn = get_input("Enter ISBN: ")

    year = get_input("Enter publishing year: ")

    try:
        price = float(input("Enter price: ").strip())
    except ValueError:
        print("Invalid input. Price should be a floating number.")
        return

    quantity = get_int_input("Enter quantity: ")
    
    book = Book(title, authors, isbn, year, price, quantity)
    library.add_book(book)
    print("Book added successfully!")

def search_books(library):
    search_term = get_input('Enter Book title or ISBN to search: ', required=False)
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
    search_term = get_input('Enter Book title or ISBN to remove: ', required=False)
    results = library.search_books(search_term)
    if results:
        print(f"\nSearch Results for '{search_term}':")
        library.display_books(results)
        try:
            book_index = get_int_input("Enter the number of the book you want to remove: ") - 1
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
    search_term = get_input('Enter Book title or ISBN to lend: ', required=False)

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
    print("+----+----------------------+-------------------------+---------------+---------------------+")
    print("| No | Title                | Authors                 | ISBN          | Borrower            |")
    print("+----+----------------------+-------------------------+---------------+---------------------+")
    for i, log in enumerate(library.lend_log):
        title = log['title'][:20].ljust(20)
        authors = ", ".join(log['authors'])[:23].ljust(23)
        isbn = log['isbn'].rjust(13)
        borrower = log['borrower'][:20].ljust(20)
        print(f"| {str(i+1).ljust(2)} | {title} | {authors} | {isbn} | {borrower} |")
        print("+----+----------------------+-------------------------+---------------+---------------------+")
    search_term = get_input('Enter Book title or ISBN to return: ', required=False)
    
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