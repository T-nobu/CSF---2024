## Overview

This test suite is designed to verify the functionality of a Library Management System built with object-oriented principles in Python. It tests interactions between core components of the system, including Book, User, Admin, and Library. The tests aim to ensure the system's correctness for key operations such as borrowing and returning books, managing book availability, and performing administrative tasks like adding new books.

The unit tests utilize the unittest framework and make use of unittest.mock to patch the standard output, allowing for the validation of messages printed by the system. The focus is on ensuring that the system behaves as expected under a variety of normal and edge cases.


## Resources Used

The test suite leverages the following components:

-unittest: The built-in Python framework for writing and running tests.
-unittest.mock.patch: A mock library tool used to capture printed output and verify user/system messages.
-StringIO: A utility from the io module to redirect printed output for inspection during tests.
-library_system.py: The main implementation file containing the Book, User, Admin, and Library classes.


## Test Cases Overview

The test suite consists of several unit tests that simulate typical user interactions with the library system. These tests cover key functionalities, including:

Borrowing Books:
Verifying that a user can successfully borrow a book.
Handling attempts to borrow unavailable or nonexistent books.

Returning Books:
Ensuring that users can return books they have borrowed.
Handling invalid return attempts, such as returning books that weren't borrowed by the user or that don't exist in the system.

Admin Functions:
Verifying that an admin can add new books to the library.

Viewing Books:
Ensuring that available and borrowed books are displayed correctly.
Test Case Details

test_borrow_book_success:
This test validates that a user can borrow a book, making it unavailable for other users. After borrowing "To Kill a Mockingbird", the book's availability status is checked, and the book is confirmed to be in the user's borrowed list.

test_borrow_book_unavailable:
This test covers the scenario where a user attempts to borrow a book that has already been borrowed by someone else. The system should display a message indicating that the book is unavailable, and the second user should not be able to borrow it.

test_return_book_success:
This test checks if a user can successfully return a book they borrowed. After returning "The Great Gatsby", the book should be marked as available again, and it should no longer appear in the user's borrowed books list.

test_return_book_not_borrowed:
In this test, a user attempts to return a book they never borrowed ("Moby Dick"). The system should correctly notify the user that they did not borrow the book.

test_admin_add_book:
This test verifies that an admin can add a new book to the library. After adding a book titled "New Book" by "Author Name", the test checks if the book appears in the library’s collection.

test_view_available_books:
This test ensures that the library correctly displays all available books. The system should print the list of available books, including "To Kill a Mockingbird", "The Great Gatsby", and "Moby Dick".

test_view_borrowed_books:
This test checks if the system correctly displays borrowed books. After borrowing "Moby Dick", the book should appear in the borrowed books list when viewed.

test_borrow_nonexistent_book:
This test covers the scenario where a user attempts to borrow a book that doesn't exist in the library’s collection. The system should print an appropriate error message stating that the book is not available.

test_return_nonexistent_book:
In this test, a user tries to return a book that doesn’t exist in the library system. The system should notify the user that they did not borrow this nonexistent book.


## Conclusion

This test suite comprehensively covers the core functionalities of the Library Management System. By simulating common user and admin interactions, the tests ensure that the system behaves correctly under both normal and edge cases. With these tests in place, the system is robust against invalid operations, such as borrowing unavailable books, and ensures accurate book management for users and administrators alike.

Future enhancements could include testing more advanced features like user authentication, overdue book penalties, and more granular admin controls.