Book Tests
TC001
Title:                  test_book_str
Test Data:              book = Book("B1234", "Test Book", "Author Name", 5)  
Test:                   str(book)                                               
Expected Output:        ID: B1234, Title: Test Book, Author: Author Name, Copies: 5


Member Tests    
TC002   
Title:                  test_borrow_book
Test Data:              member = Member("M1234", "Member Name")
                        book = Book("B1234", "Test Book", "Author Name", 5)
Test:                   member.borrow_book(book)
Expected Output:        True


TC003   
Title:                  test_borrow_book_limit
Test Data:              member = Member("M1234", "Member Name")
                        book1 = Book("B1234", "Test Book 1", "Author Name", 5)
                        book2 = Book("B1235", "Test Book 2", "Author Name", 5)
                        book3 = Book("B1236", "Test Book 3", "Author Name", 5)
                        book4 = Book("B1237", "Test Book 4", "Author Name", 5)
Precondition:           member.borrow_book(book1)
                        member.borrow_book(book2)
                        member.borrow_book(book3)
Test:                   member.borrow_book(book4)
                        book4 not in member.borrowed_books
Expected Output:        False
                        True


TC004   
Title:                  test_return_book_success
Test Data:              member = Member("M1234", "Member Name")
                        book = Book("B1234", "Test Book", "Author Name", 5)
Precondition:           member.borrow_book(book)
                        returned_book = member.returned_book(book.book_id)
Test:                   returned_book = book
                        book not in member.borrowed_books
Expected Output:        True    
                        True


TC005
Title:                  test_return_book_not_found
Test Data:              member = Member(member_id=1, name="John Doe")
Precondition:            Book being returned has not been borrowed by this member yet
Test:                   member.return_book(book_id=2)
Expected Result:        False

TC006
Title:                  test_return_book_not_borrowed
Test Data:              member = Member("M1234", "Member Name")
                        book = Book("B1234", "Test Book", "Author Name", 5)
Precondition:           returned_book = member.return_book(book.book_id)
Test:                   returned_book is None
Expected Output:        True


TC007
Title:                  test_member_str
Test Data:              member = Member("M1234", "Member Name")
Precondition:           None
Test:                   str(member)
Expected Output:        ID: M1234, Name: Member Name, Borrowed Books: None


Library Tests
TC008
Title:                  test_add_book
Precondition:           book added to library
Test Data:              added_book = self.library.books[0]
Test:                   library.add_book(title="New Book", author="Author X", copies=5)
Expected Output:        Book added: New Book


TC009
Title:                  test_add_member
Test:                   library.add_member(name="Jane Doe")
Expected Output:        Member added: ID: M____, Name: Member Name, Borrowed Books: None


TC010
Title:                  test_successful_borrow
Precondition:           library.add_book("Test Book", "Author Name", 5)
                        library.add_member("Member Name")
Test Data:              book_id = self.library.books[0].book_id
                        member_id = self.library.members[0].member_id
Test:                   library.borrow_book(member_id, book_id)
Expected Output:        Book borrowed: Test Book by Member Name


TC011
Title:                  test_no_member_found
Precondition:           Member does not exist with id 999
Test:                   library.borrow_book(member_id=999, book_id=1)
Expected Output:        No member found with ID 999

TC012
Title:                  test_no_book_found
Precondition:           Book does not exist with id 999, member with member_id exists
Test:                   library.borrow_book(member_id=member_id, book_id=999)
Expected Output:        No book found with ID 999


TC013
Title:                  test_no_copies_available
Test Data:              library.add_book("Test Book", "Author Name", 0)
                        library.add_member("Member Name")
Precondition:           book_id and member_id are known, no copies were in and none were returned
Test:                   library.borrow_book(member_id, book_id)
Expected Output:        No copies available for book: Test Book


TC014
Title:                  test_max_books_borrowed
Test Data:              4 unique books required
Precondition:           Member exists and has already borrowed 3 books
Test:                   library.borrow_book(member_id, self.librayr.book[3].book_id)
Expected Output:        Member Name has already borrowed the maximum number of books.


TC015
Title:                  test_return_book
Test Data:              library.add_book("Test Book", "Author Name", 5)
                        library.add_member("Member Name")
Precondition:            Member has borrowed the book
Test:                   library.return_book(member_id, book_id)
Expected Output:        Book returned: Test Book by Member Name


TC016
Title:                  test_return_book_not_member
Precondition:           Member does not exist with id=999
Test:                   Library.return_book(member_id=999, book_id=1)
Expected Output:        No member found with ID 999


TC017
Title:                  test_return_book_not_borrowed
Test Data:              library.add_member("Member Name")
Precondition:           Member has not borrowed this book yet.
Test:                   library.return_book(member_id, book_id=1)
Expected output:        No record of this book being borrowed by Member Name

TC018
Title:                  test_find_book
Test Data:              library.add_book("Test Book", "Author Name", 5)
Precondition:           Book and library are instantiated.
Test:                   library.find_book(book_id)
Expected Output:        


TC019
Title:                  test_find_book_not_found
Precondition:           Book with ID 999 does not exist.
Test:                   library.find_book(999)
Expected Output:        None


TC020
Title:                  test_find_member
Test Data:              library.add_member("Member Name")
Precondition:           Member ID is known.
Test:                   library.find_member(member_id)
Expected Output:        returns member


TC020
Title:                  test_find_member_not_found
Precondition:           Member with ID 999 does not exist
Test:                   library.find_member(999)
Expected Output:        Returns None


TC021
Title:                  test_display_books
Test Data:              library.add_book("Test Book 1", "Author Name", 5)
Precondition:           library contains the book with given attributes.
Test:                   library.display_books()
Expected Output:        ID: B____, Title: , Author: Author Name, Copies: 5


TC022
Title:                  test_display_books_empty
Precondition:           No books exist in the library
Test:                   library.display_books()
Expected Output:        Books in Library: 
                        No books available
TC023
Title:                  test_display_members
Test Data:              library.add_member("Member Name")
Preconditions:          Member is added to the library.
Test:                   library.display_member()
Expected Output:        "Library Members"
                        ID: M____, Name: Member Name, Borrowed Books: None"


TC024
Title:                  test_display_members_empty
Precondition:           No members are registered.
Test:                   library.display_members()
Expected Output:        Library Members:
                        No members registered.


TC025
Title:                  test_display_transactions
Precondition:           Member and book exist and member has borrowed book. Member and 
                        Book id are known
Test Data:              library.add_book("Test Book", "Author Name", 5)
                        library.add_member("Member Name")
Test:                   library.display_transactions()
Expected Output:        Transaction History:
                        Member ID: M____, Book ID: B____, Action: borrow


TC026
Title:                  test_display_transactions_empty
Precondition:           No transactions have occurred in this library.
Test:                   library.display_transactions()
Expected Output:        Transaction History:
                        No transactions yet.


Calculator Tests
TC027
Title:                  test_add
Test:                   test_add(2, 3)
Expected Output:        5


TC028
Title:                  test_subtract
Test:                   calculator.subtract(5,3)
Expected Output:        2


TC029
Title:                  test_multiply
Test:                   calculator.multiply(2,3)
Expected Output:        6


TC030
Title:                  test_divide
Test:                   calculator.divide(6, 3)
Expected Output:        2


TC031
Title:                  test_divide_by_zero
Test:                   calculator.divide(6,0)
Expected Output:        ZeroDivisionError: division by zero


TC032
Title:                  test_power
Test:                   calculator.power(2,3)
Expected Output:        8


TC033
Title: test_show_history
Precondition: calculator class
Test Data:         self.calculator.add(2, 3)
        self.calculator.subtract(5, 3)
Test: Check length of self.calculator.history, check that add and subtract are in history
Expected Output: "add(2, 3) = 5" "subtract(5, 3) = 2"

TC034
Title: test_show_history_empty
Precondition: Calculator class
Test Data: none
Test: Show history is empty
Expected Output: "No calculation history available."

TC035
Title: test_main_exit
Precondition: Main Menu
Test Data: none
Test: Input "3"
Expected Output: "Exiting the system. Goodbye!"

TC036
Title: test_invalid_main_choice
Precondition: Main Menu
Test Data: None
Test: Input "4" "3"
Expected Output: "Invalid choice. Please try again." "Exiting the system. Goodbye!"

TC037
Title: test_addition
Precondition: Main Menu, Calculator Menu, Add method
Test Data: "3" "4"
Test: Input "2", "1", "3", "4", "7", "3"
Expected Output: Check if add method is called and "Result: 7" is printed

TC038
Title: test_calculator_hisotry
Test Data: None
Precondition: Main Menu, Calculator Menu, Show Calculation History method
Test: Input "2" "6" "7" "3"
Expected Output: check if show_history method is called

TC039
Title: test_add_book
Test Data: "Test Book" "Author Name"
Precondition: Main Menu, Library Menu, Add Book
Test: Input "1" "2" "Test Book" "Author Name" "5" "8" "3"
Expected Output: "\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\nExiting the system. Goodbye!\n"

TC040
Title: test_display_books
Test Data: None
Precondition: Main Menu, Library Menu
Test: Input "1" "1" "8" "3"
Expected Output: "\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\nExiting the system. Goodbye!\n"

TC041
Title: test_invalid_input
Test Data: None
Precondition: In Main Menu
Test: Input "abc", "3"
Expected Output: "Invalid choice. Please try again."
