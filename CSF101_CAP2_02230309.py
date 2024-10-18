# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Unavailable"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"

# User class
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book_title):
        for book in library.books:
            if book.title == book_title and book.is_available:
                book.is_available = False
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed '{book.title}'.")
                return
        print(f"Sorry, '{book_title}' is not available or doesn't exist.")

    def return_book(self, library, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"{self.name} did not borrow '{book_title}'.")

# Admin class
class Admin(User):
    def add_book(self, library, title, author):
        new_book = Book(title, author)
        library.add_book(new_book)
        print(f"Admin {self.name} added '{title}' to the library.")

# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(book)

    def view_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(book)

    def view_borrowed_books(self):
        borrowed_books = [book for book in self.books if not book.is_available]
        if not borrowed_books:
            print("No borrowed books.")
        else:
            for book in borrowed_books:
                print(book)

# Main code
def main():
    # Initialing library
    library = Library()

    # Adding some predefined books
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("Moby Dick", "Herman Melville"))

    # Admin and user for demonstration
    admin = Admin("Admin123")
    user = User("Tshering Norbu")

    print("Welcome to the CST Library Management System!")
    while True:
        role = input("Are you an Admin or a User? (admin/user) Or type 'exit' to quit: ").lower()

        if role == "admin":
            password = input("Enter Admin password: ")
            if password == "Admin123":  # simple password check for demonstration
                print("\n............Accessing Admin............")
                while True:
                    print("\nAdmin Menu:")
                    print("1. View all books")
                    print("2. View available books")
                    print("3. Add a book")
                    print("4. View borrowed books with user details")
                    print("5. Exit")
                    admin_choice = input("Choose an option: ")

                    if admin_choice == "1":
                        print("\nBooks in the Library:")
                        library.view_books()
                    elif admin_choice == "2":
                        print("\nAvailable Books:")
                        library.view_available_books()
                    elif admin_choice == "3":
                        title = input("Enter the book title: ")
                        author = input("Enter the author: ")
                        admin.add_book(library, title, author)
                    elif admin_choice == "4":
                        print("\nBorrowed Books:")
                        library.view_borrowed_books()
                    elif admin_choice == "5":
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Incorrect password.")
        elif role == "user":
            while True:
                print("\nUser Menu:")
                print("1. View available books")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Exit")
                user_choice = input("Choose an option: ")

                if user_choice == "1":
                    print("\nAvailable Books:")
                    library.view_available_books()
                elif user_choice == "2":
                    book_title = input("Enter the title of the book you want to borrow: ")
                    user.borrow_book(library, book_title)
                elif user_choice == "3":
                    book_title = input("Enter the title of the book you want to return: ")
                    user.return_book(library, book_title)
                elif user_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif role == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'admin', 'user', or 'exit'.")

if __name__ == "__main__":
    main()
