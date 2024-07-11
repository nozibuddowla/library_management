class Book:
    def __init__(self, title, authors, isbn, publishing_year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.publishing_year = publishing_year
        self.price = price
        self.quantity = quantity

    def __str__(self):
        if len(self.title) > 20:
            title = (self.title[:20] + '...')
        else:
            title = self.title

        authors_str = ", ".join(self.authors)
        if len(authors_str) > 25:
            authors = authors_str[:25] + "..."
        else:
            authors = authors_str

        return f"Title: {title}\nAuthors: {authors}\nISBN: {self.isbn}\nPublishing Year: {self.publishing_year}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "isbn": self.isbn,
            "year": self.publishing_year,
            "price": self.price,
            "quantity": self.quantity
        }
    
    def from_dict(data):
        return Book(
            title = data["title"],
            authors = data["authors"],
            isbn = data["isbn"],
            publishing_year = data["year"],
            price = data["price"],
            quantity = data["quantity"]
        )