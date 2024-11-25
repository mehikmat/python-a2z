from .member import Member


class Librarian(Member):

    def __init__(self, member_id, name, email, employee_id, borrowed_books=None):
        if borrowed_books is None:
            borrowed_books = []
        super().__init__(member_id, name, email, borrowed_books)
        self.employee_id = employee_id

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book_id):
        library.remove_book(book_id)

    def __str__(self):
        base = super().__str__()
        return f"{base}, Employee ID: {self.employee_id} (Librarian)"
