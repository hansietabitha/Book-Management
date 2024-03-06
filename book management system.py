import pickle

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} - {self.genre}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book in self.books:
                print(book)

    def search_books(self, title):
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        if not found_books:
            print("No matching books found.")
        else:
            print("Matching Books:")
            for book in found_books:
                print(book)

    def delete_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                self.books.remove(book)
                print("Book deleted successfully!")
                return
        print("Book not found.")

    def save_library(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.books, file)
        print("Library saved successfully!")

    def load_library(self, filename):
        try:
            with open(filename, "rb") as file:
                self.books = pickle.load(file)
            print("Library loaded successfully!")
        except FileNotFoundError:
            print("Library file not found.")
        except Exception as e:
            print("An error occurred while loading the library.")
            print(e)

def display_menu():
    print("\nWelcome to the Book Management System!")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books")
    print("4. Delete Book")
    print("5. Save Library")
    print("6. Load Library")
    print("7. Exit")

def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            new_book = Book(title, author, genre)
            library.add_book(new_book)
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            search_title = input("Enter the title to search for: ")
            library.search_books(search_title)
        elif choice == "4":
            delete_title = input("Enter the title of the book to delete: ")
            library.delete_book(delete_title)
        elif choice == "5":
            filename = input("Enter the filename to save the library: ")
            library.save_library(filename)
        elif choice == "6":
            filename = input("Enter the filename to load the library: ")
            library.load_library(filename)
        elif choice == "7":
            print("Exiting the Book Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()