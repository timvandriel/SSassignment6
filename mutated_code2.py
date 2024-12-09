
import math
import random

class Book():

    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f'ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}'

class Member():

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if (len(self.borrowed_books) <= 3):
            return False
        self.borrowed_books.append(book)
        return True

    def return_book(self, book_id):
        for book in self.borrowed_books:
            if (book.book_id == book_id):
                self.borrowed_books.remove(book)
                return book
        return None

    def __str__(self):
        books = (', '.join([book.title for book in self.borrowed_books]) or 'None')
        return f'ID: {self.member_id}, Name: {self.name}, Borrowed Books: {books}'

class Library():

    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, title, author, copies):
        book_id = f'B{random.randint(1000, 9999)}'
        book = Book(book_id, title, author, copies)
        self.books.append(book)
        print(f'Book added: {book}')

    def add_member(self, name):
        member_id = f'M{random.randint(1000, 9999)}'
        member = Member(member_id, name)
        self.members.append(member)
        print(f'Member added: {member}')

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if (not member):
            print(f'No member found with ID {member_id}')
            return
        if (not book):
            print(f'No book found with ID {book_id}')
            return
        if (book.copies <= 0):
            print(f'No copies available for book: {book.title}')
            return
        if member.borrow_book(book):
            book.copies -= 1
            self.transactions.append((member_id, book_id, 'borrow'))
            print(f'Book borrowed: {book.title} by {member.name}')
        else:
            print(f'{member.name} has already borrowed the maximum number of books.')

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        if (not member):
            print(f'No member found with ID {member_id}')
            return
        book = member.return_book(book_id)
        if book:
            original_book = self.find_book(book_id)
            original_book.copies += 1
            self.transactions.append((member_id, book_id, 'return'))
            print(f'Book returned: {book.title} by {member.name}')
        else:
            print(f'No record of this book being borrowed by {member.name}')

    def find_book(self, book_id):
        for book in self.books:
            if (book.book_id == book_id):
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if (member.member_id == member_id):
                return member
        return None

    def display_books(self):
        print('Books in Library:')
        for book in self.books:
            print(book)
        if (not self.books):
            print('No books available.')

    def display_members(self):
        print('Library Members:')
        for member in self.members:
            print(member)
        if (not self.members):
            print('No members registered.')

    def display_transactions(self):
        print('Transaction History:')
        for transaction in self.transactions:
            (member_id, book_id, action) = transaction
            print(f'Member ID: {member_id}, Book ID: {book_id}, Action: {action}')
        if (not self.transactions):
            print('No transactions yet.')

class Calculator():

    def __init__(self):
        self.history = []
        self.memory = 0

    def add(self, a, b):
        result = (a + b)
        self.history.append(f'add({a}, {b}) = {result}')
        return result

    def subtract(self, a, b):
        result = (a - b)
        self.history.append(f'subtract({a}, {b}) = {result}')
        return result

    def multiply(self, a, b):
        result = (a * b)
        self.history.append(f'multiply({a}, {b}) = {result}')
        return result

    def divide(self, a, b):
        if (b == 0):
            raise ZeroDivisionError('division by zero')
        else:
            result = (a / b)
        self.history.append(f'divide({a}, {b}) = {result}')
        return result

    def power(self, a, b):
        result = (a ** b)
        self.history.append(f'power({a}, {b}) = {result}')
        return result

    def show_history(self):
        if (not self.history):
            print('No calculation history available.')
        else:
            for record in self.history:
                print(record)

def main():
    library = Library()
    calculator = Calculator()
    while True:
        print('\nMain Menu')
        print('1. Library Management')
        print('2. Calculator')
        print('3. Exit')
        choice = input('Enter your choice: ')
        if (choice == '1'):
            while True:
                print('\nLibrary Menu')
                print('1. Display Books')
                print('2. Add Book')
                print('3. Display Members')
                print('4. Add Member')
                print('5. Borrow Book')
                print('6. Return Book')
                print('7. Display Transactions')
                print('8. Back to Main Menu')
                library_choice = input('Enter your choice: ')
                if (library_choice == '1'):
                    library.display_books()
                elif (library_choice == '2'):
                    title = input('Enter book title: ')
                    author = input('Enter book author: ')
                    copies = int(input('Enter number of copies: '))
                    library.add_book(title, author, copies)
                elif (library_choice == '3'):
                    library.display_members()
                elif (library_choice == '4'):
                    name = input('Enter member name: ')
                    library.add_member(name)
                elif (library_choice == '5'):
                    member_id = input('Enter member ID: ')
                    book_id = input('Enter book ID: ')
                    library.borrow_book(member_id, book_id)
                elif (library_choice == '6'):
                    member_id = input('Enter member ID: ')
                    book_id = input('Enter book ID: ')
                    library.return_book(member_id, book_id)
                elif (library_choice == '7'):
                    library.display_transactions()
                elif (library_choice == '8'):
                    break
                else:
                    print('Invalid choice. Please try again.')
        elif (choice == '2'):
            while True:
                print('\nCalculator Menu')
                print('1. Add')
                print('2. Subtract')
                print('3. Multiply')
                print('4. Divide')
                print('5. Power')
                print('6. Show Calculation History')
                print('7. Back to Main Menu')
                calc_choice = input('Enter your choice: ')
                if (calc_choice == '1'):
                    a = float(input('Enter first number: '))
                    b = float(input('Enter second number: '))
                    print(f'Result: {calculator.add(a, b)}')
                elif (calc_choice == '2'):
                    a = float(input('Enter first number: '))
                    b = float(input('Enter second number: '))
                    print(f'Result: {calculator.subtract(a, b)}')
                elif (calc_choice == '3'):
                    a = float(input('Enter first number: '))
                    b = float(input('Enter second number: '))
                    print(f'Result: {calculator.multiply(a, b)}')
                elif (calc_choice == '4'):
                    a = float(input('Enter first number: '))
                    b = float(input('Enter second number: '))
                    print(f'Result: {calculator.divide(a, b)}')
                elif (calc_choice == '5'):
                    a = float(input('Enter base number: '))
                    b = float(input('Enter exponent: '))
                    print(f'Result: {calculator.power(a, b)}')
                elif (calc_choice == '6'):
                    calculator.show_history()
                elif (calc_choice == '7'):
                    break
                else:
                    print('Invalid choice. Please try again.')
        elif (choice == '3'):
            print('Exiting the system. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')
if (__name__ == '__main__'):
    main()
