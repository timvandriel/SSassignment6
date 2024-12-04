import unittest
from unittest.mock import patch
from io import StringIO
import sys
from exCode import Book, Member, Library, Calculator, main


class TestBook(unittest.TestCase):
    # Test the Book class
    def test_book_str(self):  # Test the __str__ method
        book = Book("B1234", "Test Book", "Author Name", 5)
        self.assertEqual(
            str(book), "ID: B1234, Title: Test Book, Author: Author Name, Copies: 5"
        )


class TestMember(unittest.TestCase):
    # Test the Member class
    def test_borrow_book(self):  # Test the borrow_book method
        member = Member("M1234", "Member Name")
        book = Book("B1234", "Test Book", "Author Name", 5)
        self.assertTrue(
            member.borrow_book(book)
        )  # Test the borrow_book method with success

    def test_borrow_book_limit(self):  # Test the borrow_book method with limit
        member = Member("M1234", "Member Name")
        book1 = Book("B1234", "Test Book 1", "Author Name", 5)
        book2 = Book("B1235", "Test Book 2", "Author Name", 5)
        book3 = Book("B1236", "Test Book 3", "Author Name", 5)
        book4 = Book("B1237", "Test Book 4", "Author Name", 5)
        member.borrow_book(book1)
        member.borrow_book(book2)
        member.borrow_book(book3)
        self.assertFalse(
            member.borrow_book(book4)
        )  # Test the borrow_book method with limit
        self.assertNotIn(
            book4, member.borrowed_books
        )  # Test the borrow_book method with limit

    def test_return_book_success(self):  # Test the return_book method with success
        member = Member("M1234", "Member Name")
        book = Book("B1234", "Test Book", "Author Name", 5)
        member.borrow_book(book)
        returned_book = member.return_book(book.book_id)
        self.assertEqual(returned_book, book)
        self.assertNotIn(book, member.borrowed_books)

    def test_return_book_not_found(
        self,
    ):  # Test the return_book method with book not found
        member = Member(member_id=1, name="John Doe")
        book1 = Book(book_id=1, title="Book One", author="Author A", copies=1)
        member.borrow_book(book1)
        result = member.return_book(book_id=2)
        self.assertIsNone(result)

    def test_return_book_not_borrowed(
        self,
    ):  # Test the return_book method with book not borrowed
        member = Member("M1234", "Member Name")
        book = Book("B1234", "Test Book", "Author Name", 5)
        returned_book = member.return_book(book.book_id)
        self.assertIsNone(returned_book)

    def test_member_str(self):  # Test the __str__ method
        member = Member("M1234", "Member Name")
        self.assertEqual(
            str(member), "ID: M1234, Name: Member Name, Borrowed Books: None"
        )


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Add a book
        self.library.add_book(title="New Book", author="Author X", copies=5)
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Check if the book is added to the list
        self.assertEqual(len(self.library.books), 1)
        added_book = self.library.books[0]
        # Check the book attributes
        self.assertEqual(added_book.title, "New Book")
        self.assertEqual(added_book.author, "Author X")
        self.assertEqual(added_book.copies, 5)
        # Check if the book ID is correctly formatted
        self.assertTrue(added_book.book_id.startswith("B"))
        self.assertTrue(1000 <= int(added_book.book_id[1:]) <= 9999)
        # Check the printed message
        self.assertIn(f"Book added: {added_book}", captured_output.getvalue())

    def test_add_member(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Add a member
        self.library.add_member(name="Jane Doe")
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Check if the member is added to the list
        self.assertEqual(len(self.library.members), 1)
        added_member = self.library.members[0]
        # Check the member attributes
        self.assertEqual(added_member.name, "Jane Doe")
        # Check if the member ID is correctly formatted
        self.assertTrue(added_member.member_id.startswith("M"))
        self.assertTrue(1000 <= int(added_member.member_id[1:]) <= 9999)
        # Check the printed message
        self.assertIn(f"Member added: {added_member}", captured_output.getvalue())

    def test_successful_borrow(self):
        # Add a book and a member
        self.library.add_book("Test Book", "Author Name", 5)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Borrow the book
        self.library.borrow_book(member_id, book_id)
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn(
            "Book borrowed: Test Book by Member Name", captured_output.getvalue()
        )
        # Check the book and member attributes
        self.assertEqual(self.library.books[0].copies, 4)
        self.assertEqual(len(self.library.members[0].borrowed_books), 1)
        self.assertIn((member_id, book_id, "borrow"), self.library.transactions)

    def test_no_member_found(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Borrow a book with a non-existent member ID
        self.library.borrow_book(member_id=999, book_id=1)
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("No member found with ID 999", captured_output.getvalue())

    def test_no_book_found(self):
        # Add a member
        self.library.add_member("Member Name")
        member_id = self.library.members[0].member_id
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Borrow a book with a non-existent book ID
        self.library.borrow_book(member_id=member_id, book_id=999)
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("No book found with ID 999", captured_output.getvalue())

    def test_no_copies_available(self):
        # Add a book and a member
        self.library.add_book("Test Book", "Author Name", 0)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Borrow the book
        self.library.borrow_book(member_id, book_id)
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn(
            "No copies available for book: Test Book", captured_output.getvalue()
        )

    def test_max_books_borrowed(self):
        # Add 4 books and a member
        self.library.add_book("Test Book 1", "Author Name", 1)
        self.library.add_book("Test Book 2", "Author Name", 1)
        self.library.add_book("Test Book 3", "Author Name", 1)
        self.library.add_book("Test Book 4", "Author Name", 1)
        self.library.add_member("Member Name")
        member_id = self.library.members[0].member_id
        # Borrow 3 books
        self.library.borrow_book(member_id, self.library.books[0].book_id)
        self.library.borrow_book(member_id, self.library.books[1].book_id)
        self.library.borrow_book(member_id, self.library.books[2].book_id)
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Borrow the 4th book
        self.library.borrow_book(member_id, self.library.books[3].book_id)
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn(
            "Member Name has already borrowed the maximum number of books.",
            captured_output.getvalue(),
        )

    def test_return_book(self):
        # Add a book and a member
        self.library.add_book("Test Book", "Author Name", 5)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        # Borrow the book
        self.library.borrow_book(member_id, book_id)
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Return the book
        self.library.return_book(member_id, book_id)
        sys.stdout = sys.__stdout__
        # Check the book and member attributes
        self.assertEqual(self.library.books[0].copies, 5)
        self.assertEqual(len(self.library.members[0].borrowed_books), 0)
        # Check the printed message
        self.assertIn(
            "Book returned: Test Book by Member Name", captured_output.getvalue()
        )

    def test_return_book_not_member(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Return a book with a non-existent member ID
        self.library.return_book(member_id=999, book_id=1)
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("No member found with ID 999", captured_output.getvalue())

    def test_return_book_not_borrowed(self):
        # Add a member
        self.library.add_member("Member Name")
        member_id = self.library.members[0].member_id
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Return a book that was not borrowed
        self.library.return_book(member_id, book_id=1)
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn(
            "No record of this book being borrowed by Member Name",
            captured_output.getvalue(),
        )

    def test_find_book(self):
        # Add a book
        self.library.add_book("Test Book", "Author Name", 5)
        book_id = self.library.books[0].book_id
        # Find the book
        found_book = self.library.find_book(book_id)
        self.assertEqual(found_book, self.library.books[0])

    def test_find_book_not_found(self):
        # Find a non-existent book
        found_book = self.library.find_book(999)
        self.assertIsNone(found_book)

    def test_find_member(self):
        # add a member
        self.library.add_member("Member Name")
        member_id = self.library.members[0].member_id
        found_member = self.library.find_member(member_id)
        self.assertEqual(found_member, self.library.members[0])

    def test_find_member_not_found(self):
        # Find a non-existent member
        found_member = self.library.find_member(999)
        self.assertIsNone(found_member)

    def test_display_books(self):
        # Add books
        self.library.add_book("Test Book 1", "Author Name", 5)
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Display the books
        self.library.display_books()
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("Books in Library:", captured_output.getvalue())
        self.assertIn("ID: B", captured_output.getvalue())
        self.assertIn("Title: Test Book 1", captured_output.getvalue())
        self.assertIn("Author: Author Name", captured_output.getvalue())
        self.assertIn("Copies: 5", captured_output.getvalue())

    def test_display_books_empty(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Display books when there are no books
        self.library.display_books()
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("Books in Library:", captured_output.getvalue())
        self.assertIn("No books available.", captured_output.getvalue())

    def test_display_members(self):
        # Add a member
        self.library.add_member("Member Name")
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Display members
        self.library.display_members()
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("Library Members:", captured_output.getvalue())
        self.assertIn("ID: M", captured_output.getvalue())
        self.assertIn("Name: Member Name", captured_output.getvalue())

    def test_display_members_empty(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Display members when there are no members
        self.library.display_members()
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("Library Members:", captured_output.getvalue())
        self.assertIn("No members registered.", captured_output.getvalue())

    def test_display_transactions(self):
        # Add a book and a member
        self.library.add_book("Test Book", "Author Name", 5)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        # Borrow the book
        self.library.borrow_book(member_id, book_id)
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Display the transactions
        self.library.display_transactions()
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("Transaction History:", captured_output.getvalue())
        self.assertIn(
            f"Member ID: {member_id}, Book ID: {book_id}, Action: borrow",
            captured_output.getvalue(),
        )

    def test_display_transactions_empty(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        # Display the transactions
        self.library.display_transactions()
        sys.stdout = sys.__stdout__
        # Check the printed message
        self.assertIn("No transactions", captured_output.getvalue())


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calculator.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(6, 0)

    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)

    def test_show_history(self):
        self.calculator.add(2, 3)
        self.calculator.subtract(5, 3)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calculator.show_history()
        sys.stdout = sys.__stdout__
        self.assertEqual(len(self.calculator.history), 2)
        self.assertIn("add(2, 3) = 5", captured_output.getvalue())
        self.assertIn("subtract(5, 3) = 2", captured_output.getvalue())

    def test_show_history_empty(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calculator.show_history()
        sys.stdout = sys.__stdout__
        self.assertIn("No calculation history available.", captured_output.getvalue())


class TestMainMenu(unittest.TestCase):
    # Test the main menu
    @patch("builtins.input", side_effect=["3"])  # Simulate user choosing "Exit"
    @patch("builtins.print")  # Mock the print function
    def test_main_exit(self, mock_print, mock_input):  # Test the main function
        main()  # Call the main function with mocked input
        mock_print.assert_any_call(
            "Exiting the system. Goodbye!"
        )  # Check if the exit message is printed

    @patch("builtins.input", side_effect=["4", "3"])  # Simulate invalid input then exit
    @patch("builtins.print")  # Mock the print function
    def test_invalid_main_choice(
        self, mock_print, mock_input
    ):  # Test the main function
        main()  # Call the main function with mocked input
        mock_print.assert_any_call(
            "Invalid choice. Please try again."
        )  # Check if the invalid choice message is printed
        mock_print.assert_any_call(
            "Exiting the system. Goodbye!"
        )  # Check if the exit message is printed


class TestCalculatorMenu(unittest.TestCase):
    @patch("exCode.Calculator")  # Mock Calculator class
    @patch(
        "builtins.input", side_effect=["2", "1", "3", "4", "7", "3"]
    )  # Navigate to Calculator, Add, then back to menu, then exit
    @patch("builtins.print")
    def test_addition(
        self, mock_print, mock_input, MockCalculator
    ):  # Test the add method
        mock_calculator = MockCalculator.return_value  # Create a mock calculator object
        mock_calculator.add.return_value = 7  # Set the return value of the add method
        main()  # Call the main function
        mock_calculator.add.assert_called_once_with(
            3, 4
        )  # Check if the add method is called with the correct arguments
        mock_print.assert_any_call("Result: 7")  # Check if the result is printed

    @patch("exCode.Calculator")  # Mock Calculator class
    @patch(
        "builtins.input", side_effect=["2", "6", "7", "3"]
    )  # Navigate to Calculator, Show history, then back to menu, then exit
    @patch("builtins.print")  # Mock the print function
    def test_calculator_history(
        self, mock_print, mock_input, MockCalculator
    ):  # Test the show_history method
        mock_calculator = MockCalculator.return_value  # Create a mock calculator object
        main()  # Call the main function
        mock_calculator.show_history.assert_called_once()  # Check if the show_history method is called


class TestLibraryMenu(unittest.TestCase):
    @patch("exCode.Library")  # Mock Library class
    @patch(
        "builtins.input",
        side_effect=["1", "2", "Test Book", "Author Name", "5", "8", "3"],
    )  # Navigate to Library, Add Book, then back to menu, then exit
    @patch("sys.stdout", new_callable=StringIO)  # Capture the output
    def test_add_book(
        self, mock_stdout, mock_input, MockLibrary
    ):  # Test the add_book method
        mock_library = MockLibrary.return_value  # Create a mock library object
        main()  # Call the main function
        mock_library.add_book.assert_called_once_with(
            "Test Book", "Author Name", 5
        )  # Check if the add_book method is called with the correct arguments
        self.assertIn(
            "\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\nExiting the system. Goodbye!\n",
            mock_stdout.getvalue(),
        )

    @patch("exCode.Library")
    @patch(
        "builtins.input", side_effect=["1", "1", "8", "3"]
    )  # Navigate to Library, Display Books, then back to menu, then exit
    @patch("sys.stdout", new_callable=StringIO)  # Capture the output
    def test_display_books(
        self, mock_stdout, mock_input, MockLibrary
    ):  # Test the display_books method
        mock_library = MockLibrary.return_value
        main()
        mock_library.display_books.assert_called_once()
        self.assertIn(
            "\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\nExiting the system. Goodbye!\n",
            mock_stdout.getvalue(),
        )


class TestInvalidChoices(unittest.TestCase):  # Test invalid choices
    @patch("builtins.input", side_effect=["abc", "3"])  # Invalid input then exit
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):  # Test invalid input
        main()
        self.assertIn("Invalid choice. Please try again.", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
