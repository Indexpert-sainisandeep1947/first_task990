import json
import os

class Library:
    def __init__(self):
        self.file = "library.json"
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

    def load(self):
        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, name):
        data = self.load()
        if name in data:
            print("Book already exists in the library.")
        else:
            data[name] = "Available"
            self.save(data)
            print("Book added to the library.")

    def borrow_book(self, name):
        data = self.load()
        if name in data:
            if data[name] == "Available":
                data[name] = "Borrowed"
                self.save(data)
                print("Book borrowed successfully.")
            else:
                print("Book is currently borrowed.")
        else:
            print("Book is not available in the library.")

    def return_book(self, name):
        data = self.load()
        if name in data:
            if data[name] == "Borrowed":
                data[name] = "Available"
                self.save(data)
                print("Book returned successfully.")
            else:
                print("This book wasn't borrowed.")
        else:
            print("This book does not belong to our library.")

lib = Library()

while True:
    print("\n1. Add Book to Library")
    print("2. Borrow Book from Library")
    print("3. Return Book to Library")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.add_book(input("Enter the book name to add: "))
    elif choice == "2":
        lib.borrow_book(input("Enter the book name to borrow: "))
    elif choice == "3":
        lib.return_book(input("Enter the book name to return: "))
    elif choice == "4":
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
