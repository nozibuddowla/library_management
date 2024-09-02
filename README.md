# CLI-based Library Management System

A Python-based Library Management System that allows you to add, view, search, lend, and return books. This system also keeps track of books that have been lent out, including the borrower's and returnee's information.

## Features

- **Add Book**: Add new books to the library.
- **View Books**: View all books available in the library.
- **Search Books**: Search for books by title, ISBN, or author.
- **Remove Book**: Remove books from the library.
- **Lend Book**: Lend books to users and record their information.
- **View Lent Books**: View all books that have been lent out along with the borrower's details.
- **Return Book**: Return books and verify the returnee's information.

## Installation

**Clone the repository**:
```sh
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Follow the on-screen prompts** to interact with the library system.

## File Structure

- `library.py`: Contains the `Library` class, which manages the collection of books and the lending/returning processes.
- `book.py`: Contains the `Book` class, which represents a book with attributes like title, authors, ISBN, year, price, and quantity.
- `main.py`: The main script that provides the command-line interface for interacting with the library system.
- `books.json`: A JSON file to store book data persistently.
- `lend_log.json`: A JSON file to store lending log data persistently.

## Class Descriptions

### Book Class (`book.py`)

- **Attributes**:
    - `title`: The title of the book.
    - `authors`: A list of authors of the book.
    - `isbn`: The ISBN number of the book.
    - `year`: The publishing year of the book.
    - `price`: The price of the book.
    - `quantity`: The quantity of the book available in the library.

- **Methods**:
    - `to_dict()`: Converts the book object to a dictionary for JSON serialization.
    - `from_dict()`: Creates a book object from a dictionary.

### Library Class (`library.py`)

- **Attributes**:
    - `books`: A list of book objects in the library.
    - `lend_log`: A list to keep track of lent books and their borrowers.

- **Methods**:
    - `add_book(book)`: Adds a book to the library.
    - `save_books()`: Saves the current list of books to a JSON file.
    - `load_books()`: Loads the list of books from a JSON file.
    - `save_lend_log()`: Saves the lending log to a JSON file.
    - `load_lend_log()`: Loads the lending log from a JSON file.
    - `display_books(books)`: Displays a list of books in a formatted table.
    - `view_books()`: Displays all books in the library.
    - `search_books(search_term)`: Searches for books by title or ISBN.
    - `search_books_by_author(search_term)`: Searches for books by author.
    - `remove_book(book)`: Removes a book from the library.
    - `lend_book(search_term)`: Lends a book to a user and records their information.
    - `view_lent_books()`: Displays all lent books and their borrowers' information.
    - `return_book(search_term)`: Returns a book and verifies the returnee's information.

## Examples

### Adding a Book

```sh
Enter title: The Great Gatsby
Enter authors (comma-separated): F. Scott Fitzgerald
Enter ISBN: 9780743273565
Enter publishing year: 1925
Enter price: 10.99
Enter quantity: 3
Book added successfully.