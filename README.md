# Lib50

#### Video Demo: <https://www.youtube.com/watch?v=jJ-VtniK2W8>

#### Description:
Lib50 is a simple command-line Library Management System written in Python. The program allows a library to manage books and users and provides basic functions for borrowing and returning books.

I used **OOP** (Object-Oriented Programming) because the system naturally contains different types of objects. A book has its own information and actions, a user has their own information and borrowing actions, and the library manages both. Separating these responsibilities into three classes makes the program easier to understand and organize than putting everything into one large function.

I also decided to store books and users in Python lists instead of using a database. Since this project is a simple command-line application and was mainly created to demonstrate Python programming concepts, lists were sufficient for storing the information during the program's execution. I also used dictionaries inside each user's borrowed-book list to keep track of both the book and the quantity borrowed. The program includes basic validation to ensure data integrity for books' and users' data.

## Project Architecture
The project consists of two Python files: `project.py` and `classes.py`. The `classes.py` file contains the main classes used by the system: `Book`, `User`, and `Library`.

### Book Class
Represents a book and stores its:
- Book ID
- Title
- Author
- Available quantity

It contains methods for:
- Checking whether a book is available
- Displaying book information
- Updating its quantity

### User Class
Represents a library user and stores:
- User ID
- Name
- Borrowed books

It contains methods for:
- Borrowing books
- Returning books
- Viewing the user's borrowed-book list

### Library Class
Manages the collection of books and users.

It contains methods for:
- Adding books
- Registering users
- Searching for books
- Listing all books
- Adding new books
- Viewing user information

---

### UI & Program Flow (`project.py`)
The `project.py` file contains the main program and command-line interface. It imports the classes from `classes.py` and provides a menu through which the user can interact with the library system. The available options include:

1. Viewing all books
2. Adding a new book
3. Searching for a book by title
4. Borrowing a book
5. Returning a book
6. Viewing borrowed books
7. Registering a new user
8. Viewing user information *(Admin only: password required)*
9. Exit

The program continues displaying the menu until the user chooses to exit.

## Python Libraries
- **tabulate** – to display books and users in formatted tables
- **art** – to add simple ASCII-style visual elements to the command-line interface
- **pytest** – to test custom and class functions