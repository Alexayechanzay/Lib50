from tabulate import tabulate
from art import * # for ASCII art
from classes import Book, User, Library 
ADMIN_PWD = "CS50PACZ7926"

def pwd_check(pwd):
    return pwd == ADMIN_PWD

def display_menu():
    options = [
        [1,"View all available books in the Library"],
        [2,"Add new books"],
        [3,"Search for a book by its title"],
        [4,"Borrow a book"],
        [5,"Return a book"],
        [6,"View your borrowed-book list"],
        [7,"Add new User"],
        [8,"View Users' informatoin"],
        [9,"Exit"],
    ]

    headers = ["Options","Features"]
    print(tabulate(
        options,
        headers=headers,
        tablefmt="rounded_outline",
        numalign="center",
    ))

def menu(library): # lib obj is parsed as library
    lprint(length=100,height=1,char="*")
    tprint("Welcome   to  Lib50")
    lprint(length=100,height=1,char="*")
    while True:
        display_menu()
        option = int(input("Plz enter your choice: (e.g: 1) ").strip())

        if option == 1:
            library.list_books()

        elif option == 2:
            library.add_new_book()

        elif option == 3:
            title = input("Plz enter the title of book: ").lstrip()
            found_books = library.search_book(title)

            if found_books:
                table_data = [
                    [book.book_id, book.title, book.author, book.quantity]
                    for book in found_books
                ]
                headers = ["Book ID", "Title", "Author", "Quantity"]
                print("\nSearch results:\n")
                print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))
            else:
                print(f"No book with the title '{title}' was found 🤔")

        elif option == 4:
            user_id = int(input("Plz enter your user id: "))
            book_id = int(input("Plz enter book id you want to borrow: "))

            # ID validation 
            # next is used to find the first match
            user = next((usr for usr in library.users if usr.user_id == user_id),None)
            book = next((bk for bk in library.books if bk.book_id == book_id),None)

            if user and book:
                user.borrow_book(book)
            else:
                print("Invalid user or book id :(")

        elif option == 5:
            user_id = int(input("Plz enter your user id: "))
            book_id = int(input("Plz enter Book ID you want to return: "))
        
            # ID validation 
            # next is used to find the first match
            user = next((usr for usr in library.users if usr.user_id == user_id),None)
            book = next((bk for bk in library.books if bk.book_id == book_id),None)

            if user and book:
                user.return_book(book)
            else:
                lprint(length=27,height=1,char="*")
                print("Invalid user or book id :(")
                lprint(length=27,height=1,char="*")

        elif option == 6: # view borrowed-book list
            user_id = int(input("Plz enter your user id: "))
            u = next((usr for usr in library.users if usr.user_id == user_id), None)

            if u:
                u.view_borrowed_bookList()
            else:
                lprint(length=17,height=1,char="*")
                print("Invalid User ID!")
                lprint(length=17,height=1,char="*")

        elif option == 8:
            pwd = input("Enter the password: ")
            if pwd_check(pwd):
                library.view_users_info()
            else:
                lprint(length=35,height=1,char="*")
                print("Cannot Access to User Information!")
                lprint(length=35,height=1,char="*")

        elif option == 7:
            while True:
                user_id = int(input("Plz enter user id: "))
                name = input("Plz enter your name: ").strip()
                new_user = User(user_id, name)

                if library.register_user(new_user):
                    break
                else:
                    lprint(length=34,height=1,char="*")
                    print("Please enter a different user ID.")
                    lprint(length=34,height=1,char="*")

        elif option == 9:
            tprint("Bye for now!")
            break # IMPORTANT   
        else:
            print(text2art("Invalid choice!",font="small"))
            print(text2art("Plz try again!",font="small"))


def main():
    # Initializing LMS system 
    # Lib instance (obj)
    library = Library()
    # add some books 
    b1 = Book(1,"Atomic Habbit","James Clear", 10)
    b2 = Book(2,"Gone with the Wind", "Margaret Mitchel",5)
    b3 = Book(3, "Crime and Punishment", "Fyodor Dostoevsky",2)
    b4 = Book(4,"Elon Musk", "Walter Isaacson", 10)
    b5 = Book(5, "Dar Taung Ko Kyaw Yae Mi Pin Lae Ko Pyat Mye", "Mya Than Tint",10)

    # add some users
    #usr1 = User(1,"Aye Chan Zay")

    # add books and users to LMS
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    library.add_book(b4)
    library.add_book(b5)

    menu(library)

if __name__ == "__main__":
    main()