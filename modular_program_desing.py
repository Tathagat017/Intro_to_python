
bookShelf = []


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def AddBook(book):
    bookShelf.append(Book(book))
    print(f"Book '{book}' added to the shelf.")

def SearchBook(book):
    for b in bookShelf:
        if b.name.lower() == book.lower():
            print(f"Book '{b.name}' found on the shelf.")
            return
    print(f"Book '{book}' not found on the shelf.")

def DisplayInventory():
    if not bookShelf:
        print("No books in the shelf.")
    else:
        print("Books in the shelf:")
        for b in bookShelf:
            print(f"- {b.name}")




def Main():
    print("Welcome to the Library Management System")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Display all books")
    print("4. Exit")
    flag = True
    while(flag):
        userChoice = input("Enter your choice: ")
        if userChoice == "1":
            book = input("Enter the book name to add: ")
            AddBook(book)
        elif userChoice == "2":
            searchedBook = input("Enter the book name to search: ")
            SearchBook(searchedBook)
        elif userChoice == "3":
            DisplayInventory()
        elif userChoice == "4":
            print("Exiting the program.")
            flag = False
     

if __name__ == "__main__":
    print("library: modular_program_design")
    Main()