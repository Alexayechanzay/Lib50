from tabulate import tabulate
from art import *

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.author = author 
        self.title = title # book title 
        self.quantity = quantity #  No of books available 

    # methods of Book class  (aka: features)
    def check_availability(self):
        """
        Description: Check the availability of book based on its quantity
        Type: TRUE/FALSE 
        """
        return self.quantity > 0

    def display_book_info(self):
        """
        Description: Display the book's detailed information (ID, Author, Title, Quantity)
        Type: String
        """
        table_data = [[self.book_id, self.title, self.author, self.quantity]]
        headers = ["Book ID", "Title", "Author", "Quantity"]
        print(tabulate(
            table_data,
            headers=headers,
            tablefmt="rounded_outline",
            numalign="center",
            stralign="left",
        ))

    def update_quantity(self, quantity):
        """
        Descripton: Display the number of available book based on borrowing or returning
        Type: Integer
        """
        self.quantity += quantity 

class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name  =  user_name
        self.borrowed_bookList = [] # a list of borrowed entries: {'book': book, 'quantity': count}

    # methods of Student 
    def borrow_book(self, book): # book (parameter) => book that std wants 
        """
        Description: Borrow a book from the Library if it's available
        """
        if book.check_availability(): # calling Book's method
            existing_entry = next((entry for entry in self.borrowed_bookList if entry["book"].book_id == book.book_id), None)

            if existing_entry is not None: # if same is borrowed again, qty is just incremented
                existing_entry["quantity"] += 1
            else:
                self.borrowed_bookList.append({"book": book, "quantity": 1})

            book.update_quantity(-1)
            text = f"{self.user_name} has successfully borrowed '{book.title}' :)"
            lprint(length=len(text), height=1, char="*")
            print(text)
            lprint(length=len(text), height=1, char="*")
        else:
            text2 = f"Sorry, '{book.title}' is not currently available :("
            lprint(length=len(text2), height=1, char="*")
            print(text2)
            lprint(length=len(text2), height=1, char="*")

    def return_book(self, book):
        """
        Description: Return a borrowed book to the Library
        """
        existing_entry = next((entry for entry in self.borrowed_bookList if entry["book"].book_id == book.book_id), None)

        if existing_entry is not None:
            if existing_entry["quantity"] > 1:
                existing_entry["quantity"] -= 1
            else:
                self.borrowed_bookList.remove(existing_entry)
            book.update_quantity(1)
            print(f"{self.user_name} has successfully returned '{book.title}' :)")
        else:
            t1 = f"{self.user_name} does not have '{book.title}' borrowed :O"
            print(f"{self.user_name} does not have '{book.title}' borrowed :O")

    def view_borrowed_bookList(self):
        """
         View the list of borrowed books by the user
        """
        if self.borrowed_bookList:
            print(f"{self.user_name}'s borrowed books")
            table_data = [
                [entry["book"].book_id, entry["book"].title, entry["book"].author, entry["quantity"]]
                for entry in self.borrowed_bookList
            ]
            headers = ["Book ID", "Title", "Author", "Quantity"]
            print(tabulate(
                table_data,
                headers=headers,
                tablefmt="rounded_outline",
                numalign="center",
                stralign="left",
            ))
        else:
            print(f"{self.user_name} has not borrowed any books 🧐")

class Library:
    def __init__(self):
        self.books = [] # list of all Library boooks (Book Storage)
        self.users = [] # list of all users (User Storage)

    # Library's methods 
    def add_book(self, book):
        """
        Description: Add a book to the Library
        """
        self.books.append(book)

    def register_user(self, user):
        """
        Description: Registers a new user to the system, ensuring that no duplicate user IDs exist
        """
        if any(curr_user.user_id == user.user_id for curr_user in self.users):
            print(f"User with the same ID has already existed! Try another ID :|")
            return False

        self.users.append(user)
        print(f"New user {user.user_name} has been successfully added to the Library :)")
        return True

    def search_book(self, title):
        """
        Description: Search book by title and return the found books
        """
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def list_books(self):
        """
        Description: List all the books in the library
        """
        if self.books:
            print("Available books in the Library\n")
            table_data = [
                [book.book_id, book.title, book.author, book.quantity]
                for book in self.books
            ]
            headers = ["Book ID", "Title", "Author", "Quantity"]
            print(tabulate(
                table_data,
                headers=headers,
                tablefmt="rounded_outline",
                numalign="center",
                stralign="left",
            ))
        else:
            print(f"Currently, No books available at the Library :(")

    def add_new_book(self):
        """
        Description: Add a new book to the Library
        """
        while True:
            new_book_id = int(input("Plz enter the book id: ").strip())
            if any(book.book_id == new_book_id for book in self.books):
                print(f"Book with the same ID has already existed! Try another ID :|")
                continue
            print(f"Book ID {new_book_id} is valid!")
            break

        title = input("Plz enter the book title: ").strip()
        author = input("Plz enter the author of the book: ").strip()
        quantity = int(input("Plz enter the quantity of the book: ").strip())

        new_book = Book(new_book_id, title, author, quantity)
        self.add_book(new_book)
        print("New book has been successfully added :)")
        new_book.display_book_info()

    def view_users_info(self):
        """
        Description: View added uers information 
        """
        table_data = [
            [u.user_id, u.user_name,[[bk["book"].title,bk["quantity"]]  for bk in u.borrowed_bookList]]
            for u in self.users
        ]

        headers = ["User ID", "User Name", "Borrowed-book list"]
        print(tabulate(
            table_data,
            headers,
            tablefmt="rounded_outline",
            numalign="center"
        ))

    