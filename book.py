class Book:
    def __init__(self, title, authors, isbn, publishing_year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.publishing_year = publishing_year
        self.price = price
        self.quantity = quantity

    def __str__(self):
        authors_str = ", ".join(self.authors)
        return f"Title: {self.title}\nAuthors: {authors_str}\nISBN: {self.isbn}\nPublishing Year: {self.publishing_year}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "isbn": self.isbn,
            "year": self.publishing_year,
            "price": self.price,
            "quantity": self.quantity
        }