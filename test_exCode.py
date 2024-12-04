import unittest
from exCode import Book, Member, Library, Calculator


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("B1234", "Test Book", "Author Name", 5)
        self.assertEqual(book.book_id, "B1234")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.copies, 5)

    def test_book_str(self):
        book = Book("B1234", "Test Book", "Author Name", 5)
        self.assertEqual(
            str(book), "ID: B1234, Title: Test Book, Author: Author Name, Copies: 5"
        )


class TestMember(unittest.TestCase):
    def test_member_creation(self):
        member = Member("M1234", "Member Name")
        self.assertEqual(member.member_id, "M1234")
        self.assertEqual(member.name, "Member Name")
        self.assertEqual(member.borrowed_books, [])

    def test_borrow_book(self):
        member = Member("M1234", "Member Name")
        book = Book("B1234", "Test Book", "Author Name", 5)
        book1 = Book("B1235", "Test Book 1", "Author Name", 5)
        book2 = Book("B1236", "Test Book 2", "Author Name", 5)
        book3 = Book("B1237", "Test Book 3", "Author Name", 5)
        self.assertTrue(member.borrow_book(book))
        self.assertTrue(member.borrow_book(book1))
        self.assertTrue(member.borrow_book(book2))
        self.assertIn(book, member.borrowed_books)
        self.assertFalse(member.borrow_book(book3))

    def test_borrow_book_limit(self):
        member = Member("M1234", "Member Name")
        book1 = Book("B1234", "Test Book 1", "Author Name", 5)
        book2 = Book("B1235", "Test Book 2", "Author Name", 5)
        book3 = Book("B1236", "Test Book 3", "Author Name", 5)
        book4 = Book("B1237", "Test Book 4", "Author Name", 5)
        member.borrow_book(book1)
        member.borrow_book(book2)
        member.borrow_book(book3)
        self.assertFalse(member.borrow_book(book4))
        self.assertNotIn(book4, member.borrowed_books)

    def test_return_book_success(self):
        member = Member("M1234", "Member Name")
        book = Book("B1234", "Test Book", "Author Name", 5)
        member.borrow_book(book)
        returned_book = member.return_book(book.book_id)
        self.assertEqual(returned_book, book)
        self.assertNotIn(book, member.borrowed_books)

    def test_return_book_not_found(self):
        member = Member(member_id=1, name="John Doe")
        book1 = Book(book_id=1, title="Book One", author="Author A", copies=1)
        member.borrow_book(book1)
        result = member.return_book(book_id=2)
        self.assertIsNone(result)

    def test_return_book_not_borrowed(self):
        member = Member("M1234", "Member Name")
        book = Book("B1234", "Test Book", "Author Name", 5)
        returned_book = member.return_book(book.book_id)
        self.assertIsNone(returned_book)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Test Book", "Author Name", 5)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_add_member(self):
        self.library.add_member("Member Name")
        self.assertEqual(len(self.library.members), 1)
        self.assertEqual(self.library.members[0].name, "Member Name")

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
