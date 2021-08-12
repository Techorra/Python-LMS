class Library:
    def __init__(self, List_of_books):
        self.books = List_of_books

    def Display_available_books(self):
        print("\nBooks present in this library are: ")

        for book in self.books:
            print(f"\t * {book}")

    def Borrow_book(self, Book_name):
        if Book_name in self.books:
            print(f"""
                You have been issued {Book_name}. 
                Please Keep it safe and return it within 30 days
                   """)

            self.books.remove(Book_name)
            return True

        else:
            print("""
                    Sorry, This book is either not available or has already 
                    been issued to someoneelse. Please wait until the 
                    book is available
                  """)

            return False

    def Return_book(self, Book_name):
        self.books.append(Book_name)

        print("""
                  Thanks for returning this book! Hope you enjoyed reading 
                  it. Have a greate day ahead!
              """)


class Student:
    def Request_book(self):
        self.book = (input("Enter the name of the book you want to borrow: "))
        return self.book

    def Return_book(self):
        self.book = (input("Enter the name of the book you want to Return: "))
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django",
                             "Python Notes", "CLRS"])
    student = Student()

    while (True):
        Welcome_msg = '''
        ===== Welcome to Central Library =====
        Please choose an option:
            1.List all the books
            2.Request a book
            3.Add/Return a book
            4.Exit the Library
                    '''
        print(Welcome_msg)

        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.Display_available_books()
        elif a == 2:
            centraLibrary.Borrow_book(student.Request_book())
        elif a == 3:
            centraLibrary.Return_book(student.Return_book())
        elif a == 4:
            print("Thank's for Using Central Library! Have a greate day ahead")
            exit()
        else:
            print("Invalid Choice!")
