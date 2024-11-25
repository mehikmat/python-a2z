class Member:

    def __init__(self, member_id, name, email, borrowed_books=None):
        if borrowed_books is None:
            borrowed_books = []
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": [vars(book) for book in self.borrowed_books]
        }

    def __str__(self):
        borrowed = ', '.join([book.title for book in self.borrowed_books]) or 'None'
        return f"ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Borrowed Books: {borrowed}"
