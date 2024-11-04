import unittest
from unittest.mock import patch
from io import StringIO
from CSF101_CAP2_02230309 import Book, User, Admin, Library 

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        # setting up library, user, and admin
        self.library = Library()
        self.user = User("Tshering Norbu")
        self.admin = Admin("Admin123")

        # adding books to the library
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
        self.book3 = Book("Moby Dick", "Herman Melville")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

    def test_borrow_book_success(self):
        self.user.borrow_book(self.library, "To Kill a Mockingbird")
        self.assertFalse(self.book1.is_available, "Book should not be available after borrowing")
        self.assertIn(self.book1, self.user.borrowed_books, "Book should be in user's borrowed books list")

    def test_borrow_book_unavailable(self):
        # user borrows the book
        self.user.borrow_book(self.library, "To Kill a Mockingbird")
        another_user = User("Another User")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            another_user.borrow_book(self.library, "To Kill a Mockingbird")
            self.assertIn("Sorry, 'To Kill a Mockingbird' is not available or doesn't exist.", mock_stdout.getvalue())

        self.assertNotIn(self.book1, another_user.borrowed_books, "Another user should not be able to borrow an unavailable book")

    def test_return_book_success(self):
        self.user.borrow_book(self.library, "The Great Gatsby")
        self.user.return_book(self.library, "The Great Gatsby")

        self.assertTrue(self.book2.is_available, "Book should be available after returning")
        self.assertNotIn(self.book2, self.user.borrowed_books, "Book should be removed from user's borrowed books after returning")

    def test_return_book_not_borrowed(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.user.return_book(self.library, "Moby Dick")
            self.assertIn("Tshering Norbu did not borrow 'Moby Dick'.", mock_stdout.getvalue())

    def test_admin_add_book(self):
        self.admin.add_book(self.library, "New Book", "Author Name")
        
        added_book = next(book for book in self.library.books if book.title == "New Book")
        self.assertIsNotNone(added_book, "The new book should be in the library's collection")
        self.assertIn(added_book, self.library.books, "The newly added book should be in the library's books list")

    def test_view_available_books(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.library.view_available_books()
            output = mock_stdout.getvalue()
            self.assertIn("To Kill a Mockingbird", output)
            self.assertIn("The Great Gatsby", output)
            self.assertIn("Moby Dick", output)

    def test_view_borrowed_books(self):
        self.user.borrow_book(self.library, "Moby Dick")
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.library.view_borrowed_books()
            output = mock_stdout.getvalue()
            self.assertIn("Moby Dick", output)

    def test_borrow_nonexistent_book(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.user.borrow_book(self.library, "Nonexistent Book")
            self.assertIn("Sorry, 'Nonexistent Book' is not available or doesn't exist.", mock_stdout.getvalue())

    def test_return_nonexistent_book(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.user.return_book(self.library, "Nonexistent Book")
            self.assertIn("Tshering Norbu did not borrow 'Nonexistent Book'.", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
