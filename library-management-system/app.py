import json

from library import Library, Member, Librarian, Book


def main():
    library = Library()
    load_data(library)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book (Librarian)")
        print("2. Remove Book (Librarian)")
        print("3. Register Member")
        print("4. Remove Member")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. List Books")
        print("8. List Members")
        print("9. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                librarian_id = input("Enter Librarian ID: ")
                if librarian_id not in library.members:
                    print("Librarian not found.")
                    continue
                librarian = library.members[librarian_id]
                if not isinstance(librarian, Librarian):
                    print("User is not a librarian.")
                    continue
                book_id = input("Enter Book ID: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                copies = int(input("Enter number of copies: "))
                book = Book(book_id, title, author, copies)
                librarian.add_book(library, book)
                print("Book added successfully.")

            elif choice == '2':
                librarian_id = input("Enter Librarian ID: ")
                if librarian_id not in library.members:
                    print("Librarian not found.")
                    continue
                librarian = library.members[librarian_id]
                if not isinstance(librarian, Librarian):
                    print("User is not a librarian.")
                    continue
                book_id = input("Enter Book ID to remove: ")
                librarian.remove_book(library, book_id)
                print("Book removed successfully.")

            elif choice == '3':
                member_id = input("Enter Member ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                role = input("Is this user a Librarian? (y/n): ").lower()
                if role == 'y':
                    employee_id = input("Enter Employee ID: ")
                    member = Librarian(member_id, name, email, employee_id)
                else:
                    member = Member(member_id, name, email)
                library.register_member(member)
                print("Member registered successfully.")

            elif choice == '4':
                member_id = input("Enter Member ID to remove: ")
                library.remove_member(member_id)
                print("Member removed successfully.")

            elif choice == '5':
                member_id = input("Enter Member ID: ")
                book_id = input("Enter Book ID to borrow: ")
                library.borrow_book(member_id, book_id)
                print("Book borrowed successfully.")

            elif choice == '6':
                member_id = input("Enter Member ID: ")
                book_id = input("Enter Book ID to return: ")
                library.return_book(member_id, book_id)
                print("Book returned successfully.")

            elif choice == '7':
                books = library.list_books()
                print("\nBooks in Library:")
                for book in books:
                    print(book)

            elif choice == '8':
                members = library.list_members()
                print("\nLibrary Members:")
                for member in members:
                    print(member)

            elif choice == '9':
                save_data(library)
                print("Data saved. Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def load_data(library):
    try:
        with open('data/books.json', 'r') as f:
            books_data = json.load(f)
            for b in books_data:
                book = Book(**b)
                library.add_book(book)
    except FileNotFoundError:
        print("books.json not found. Starting with an empty book list.")

    try:
        with open('data/members.json', 'r') as f:
            members_data = json.load(f)
            for m in members_data:
                borrowed_books = [Book(**b) for b in m.get("borrowed_books")]
                m["borrowed_books"] = borrowed_books
                if m.get('employee_id'):
                    member = Librarian(**m)
                else:
                    member = Member(**m)

                library.register_member(member)
    except FileNotFoundError:
        print("members.json not found. Starting with an empty member list.")


def save_data(library):
    books_data = [vars(book) for book in library.list_books()]
    with open('data/books.json', 'w') as f:
        json.dump(books_data, f, indent=4)

    # vars only work for top level class attributes but doesn't handle nested objects like borrowed_books.
    members_data = [member.to_dict() for member in library.list_members()]
    with open('data/members.json', 'w') as f:
        json.dump(members_data, f, indent=4)


if __name__ == "__main__":
    main()
