#This is a Library Management Program
#You can add any slow relaxing music which plays in background in library
from pygame import mixer

mixer.init()
mixer.music.load("file.mp3")
mixer.music.set_volume(0.05)
mixer.music.play()


class Library:
    def __init__(self, list_of_books, library_name):
        self.books = list_of_books
        self.lib_name = library_name
        self.landed_books = {}

    def display_available(self):
        for book_name in self.books:
            if book_name not in self.landed_books:
                print(book_name)

    def display_books(self):
        for book in self.books:
            print(book)

    def land_books(self, book_name, name_of_lander):
        if book_name in self.books:
            if book_name not in self.landed_books:
                self.landed_books.update({book_name: name_of_lander})
                print("Book Landed Successfully")
            else:
                print(f"Book is already landed.\nBook now belongs to {self.landed_books.get(book_name)}.")
        else:
            print("Sorry Book is not in our library.")

    def add_book(self,book_name):
        self.books.append(book_name)
        print("Book Added Successfully.")

    def return_book(self, book_name):
        if book_name in self.landed_books:
            self.landed_books.pop(book_name)
            print("Book Returned successfully.")
        else:
            print(f"This book \"{book_name}\" is not landed from our library.")


book_names = ["The Guide", "A Fine Balance", "Smarter Faster Better", "The Secret", "Think and Grow Rich", "Drive"]

if __name__ == '__main__':
    rohit_libs = Library(book_names, "Wisy Libraries")
    while True:
        print("\nEnter one of the following options to perform the action.")
        print("1.Display Books in Library\n2.Land A Book\n3.Add A Book\n4.Return A Book\n5.Print Available Books\n6.Exit")
        choice = input("Enter your choice : ")

        if choice == "1":
            print("Book Names Are - ")
            rohit_libs.display_books()
        elif choice == "2":
            print("Lits of Books in Our Library --")
            rohit_libs.display_books()
            book = input("Enter book name you want to land : ")
            name = input("Enter your name : ")
            rohit_libs.land_books(book, name)
        elif choice == "3":
            book = input("Enter book name : ")
            rohit_libs.add_book(book)
        elif choice == "4":
            book = input("Enter book name to return : ")
            rohit_libs.return_book(book)
        elif choice == "5":
            rohit_libs.display_available()
        elif choice == "6":
            break
        else:
            print("Please enter correct option")

