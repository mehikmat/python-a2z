class Book:

    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Id: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}"
