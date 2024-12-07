Book Tests
TC001
Title:                  test_book_str
Test Data:              book = Book("B1234", "Test Book", "Author Name", 5)  
Precondition:           None   
Test:                   str(book)                                               
Expected Output:        ID: B1234, Title: Test Book, Author: Author Name, Copies: 5


Member Tests    
TC002   
Title:                  test_borrow_book
Test Data:              member = Member("M1234", "Member Name")
                        book = Book("B1234", "Test Book", "Author Name", 5)
Precondition:           None
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
Precodition:            Book being returned has not been borrowed by this member yet
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
Expected Output:        "ID: M1234, Name: Member Name, Borrowed Books: None"


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
Expected Output:        Member added: Jane Doe


TC010
Title:                  test_successful_borrow
Precondition:           library.add_book("Test Book", "Author Name", 5)
                        library.add_member("Member Name")
Test Data:              book_id = self.library.books[0].book_id
                        member_id = self.library.members[0].member_id
Test:                   library.borrow_book(member_id, book_id)
Expected Output:        "Book borrowed: Test Book by Member Name"


TC011
Title:                  test_no_member_found
Precondition:           Member does not exist with id 999
Test:                   library.borrow_book(member_id=999, book_id=1)
Expected Output:        "No member found with ID 999"

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
Expected Output:        "No copies available for book: Test Book"


TC014
Title:                  test_max_books_borrowed
Test Data:              4 unique books required
Precondition:           Member exists and has already borrowed 3 books
Test:                   library.borrow_book(member_id, self.librayr.book[3].book_id)
Expected Output:        "Member Name has already borrowed the maximum number of books."


TC015
Title:                  


TC034
Title: test_show_history
Precondition: calculator class
Test Data:         self.calculator.add(2, 3)
        self.calculator.subtract(5, 3)
Test: Check length of self.calculator.history, check that add and subtract are in history
Expected Output: "add(2, 3) = 5" "subtract(5, 3) = 2"

TC035
Title: test_show_history_empty
Precondition: Calculator class
Test Data: none
Test: Show history is empty
Expected Output: "No calculation history available."

TC036
Title: test_main_exit
Precondition: Main Menu
Test Data: none
Test: Input "3"
Expected Output: "Exiting the system. Goodbye!"

TC037
Title: test_invalid_main_choice
Precondition: Main Menu
Test Data: None
Test: Input "4" "3"
Expected Output: "Invalid choice. Please try again." "Exiting the system. Goodbye!"

TC038
Title: test_addition
Precondition: Main Menu, Calculator Menu, Add method
Test Data: "3" "4"
Test: Input "2", "1", "3", "4", "7", "3"
Expected Ouput: Check if add method is called and "Result: 7" is printed

TC039
Title: test_calculator_hisotry
Test Data: None
Precondition: Main Menu, Calculator Menu, Show Calculation History method
Test: Input "2" "6" "7" "3"
Expected Output: check if show_history method is called

TC040
Title: test_add_book
Test Data: "Test Book" "Author Name"
Precondition: Main Menu, Library Menu, Add Book
Test: Input "1" "2" "Test Book" "Author Name" "5" "8" "3"
Expected Output: "\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\nExiting the system. Goodbye!\n"

TC041
Title: test_display_books
Test Data: None
Precondition: Main Menu, Library Menu
Test: Input "1" "1" "8" "3"
Expected Output: "\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nLibrary Menu\n1. Display Books\n2. Add Book\n3. Display Members\n4. Add Member\n5. Borrow Book\n6. Return Book\n7. Display Transactions\n8. Back to Main Menu\n\nMain Menu\n1. Library Management\n2. Calculator\n3. Exit\nExiting the system. Goodbye!\n"

TC042
Title: test_invalid_input
Test Data: None
Precondtiion: In Main Menu
Test: Input "abc", "3"
Expected Output: "Invalid choice. Please try again."

