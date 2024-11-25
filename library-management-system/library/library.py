class Library:
    def __init__(self):
        self.books = {}  # key: book_id, value: Book instance
        self.members = {}  # key: member_id, value: Member or Librarian instance

    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
        else:
            self.books[book.book_id] = book

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            raise ValueError("Book ID not found.")

    def register_member(self, member):
        if member.member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
        else:
            raise ValueError("Member ID not found.")

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member ID not found.")
        if book_id not in self.books:
            raise ValueError("Book ID not found.")
        book = self.books[book_id]
        member = self.members[member_id]
        if book.copies < 1:
            raise ValueError("No copies available.")
        book.copies -= 1
        member.borrow_book(book)

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member ID not found.")
        if book_id not in self.books:
            raise ValueError("Book ID not found.")
        book = self.books[book_id]
        member = self.members[member_id]
        if book not in member.borrowed_books:
            raise ValueError("This book was not borrowed by the member.")
        book.copies += 1
        member.return_book(book)

    def list_books(self):
        return list(self.books.values())

    def list_members(self):
        return list(self.members.values())
