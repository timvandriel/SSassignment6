import unittest
from io import StringIO
import sys
from exCode import Book, Member, Library, Calculator


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

    def test_borrow_book(self):
        self.library.add_book("Test Book", "Author Name", 5)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, book_id)
        self.assertEqual(self.library.books[0].copies, 4)
        self.assertEqual(len(self.library.members[0].borrowed_books), 1)

    def test_return_book(self):
        self.library.add_book("Test Book", "Author Name", 5)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, book_id)
        self.library.return_book(member_id, book_id)
        self.assertEqual(self.library.books[0].copies, 5)
        self.assertEqual(len(self.library.members[0].borrowed_books), 0)

    def test_no_member_found(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.library.borrow_book(member_id=999, book_id=1)
        sys.stdout = sys.__stdout__
        self.assertIn("No member found with ID 999", captured_output.getvalue())

    def test_no_book_found(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.library.borrow_book(member_id=1, book_id=999)
        sys.stdout = sys.__stdout__
        self.assertIn("No book found with ID 999", captured_output.getvalue())

    def test_no_copies_available(self):
        self.library.add_book("Test Book", "Author Name", 0)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        captured_output = StringIO()
        sys.stdout = captured_output
        self.library.borrow_book(member_id, book_id)
        sys.stdout = sys.__stdout__
        self.assertIn(
            "No copies available for book: Test Book", captured_output.getvalue()
        )

    def test_successful_borrow(self):
        self.library.add_book("Test Book", "Author Name", 5)
        self.library.add_member("Member Name")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        captured_output = StringIO()
        sys.stdout = captured_output
        self.library.borrow_book(member_id, book_id)
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Book borrowed: Test Book by Member Name", captured_output.getvalue()
        )
        self.assertEqual(self.library.books[0].copies, 4)
        self.assertIn((member_id, book_id, "borrow"), self.library.transactions)

    def test_max_books_borrowed(self):
        self.library.add_book("Test Book 1", "Author Name", 1)
        self.library.add_book("Test Book 2", "Author Name", 1)
        self.library.add_book("Test Book 3", "Author Name", 1)
        self.library.add_book("Test Book 4", "Author Name", 1)
        self.library.add_member("Member Name")
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, self.library.books[0].book_id)
        self.library.borrow_book(member_id, self.library.books[1].book_id)
        self.library.borrow_book(member_id, self.library.books[2].book_id)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.library.borrow_book(member_id, self.library.books[3].book_id)
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Member Name has already borrowed the maximum number of books.",
            captured_output.getvalue(),
        )


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)
        result = self.calculator.add(-2, -3)
        self.assertEqual(result, -5)
        result = self.calculator.add(2, -3)
        self.assertEqual(result, -1)

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)
        result = self.calculator.subtract(-5, -3)
        self.assertEqual(result, -2)
        result = self.calculator.subtract(5, -3)
        self.assertEqual(result, 8)

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)
        result = self.calculator.multiply(-2, -3)
        self.assertEqual(result, 6)
        result = self.calculator.multiply(2, -3)
        self.assertEqual(result, -6)

    def test_divide(self):
        result = self.calculator.divide(6, 3)
        self.assertEqual(result, 2)
        result = self.calculator.divide(-6, -3)
        self.assertEqual(result, 2)
        result = self.calculator.divide(6, -3)
        self.assertEqual(result, -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(6, 0)

    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)
        result = self.calculator.power(-2, 3)
        self.assertEqual(result, -8)
        result = self.calculator.power(2, 0)
        self.assertEqual(result, 1)

    def test_show_history(self):
        self.calculator.add(2, 3)
        self.calculator.subtract(5, 3)
        self.calculator.show_history()
        self.assertEqual(len(self.calculator.history), 2)


if __name__ == "__main__":
    unittest.main()
