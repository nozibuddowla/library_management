class Book:
    def __init__(self, title, authors, isbn, publishing_year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.publishing_year = publishing_year
        self.price = price
        self.quantity = quantity

    
    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "isbn": self.isbn,
            "publishing_year": self.publishing_year,
            "price": self.price,
            "quantity": self.quantity
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            authors=data['authors'],
            isbn=data['isbn'],
            publishing_year=data["publishing_year"],
            price=data['price'],
            quantity=data['quantity']
        )