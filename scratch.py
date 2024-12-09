from exCode import Member, Library, Book, Calculator

library = Library()
library.add_member("Member Name")
library.add_book("Test Book", "Author Name", 5)
#library.add_member("Member Name")
book_id = library.books[0].book_id
member_id = library.members[0].member_id
library.borrow_book(member_id, book_id)
library.return_book(member_id, book_id)
#library.display_transactions()

#calculator = Calculator()
#calculator.divide(6, 0)