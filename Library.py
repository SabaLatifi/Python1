from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @abstractmethod
    def display_info(self):
        pass


class Book(Item):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def display_info(self):
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}"


class Magazine(Item):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue

    def display_info(self):
        return f"Magazine: {self.title}, Author: {self.author}, Year: {self.year}, Issue: {self.issue}"


class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow(self, item):
        self.borrowed_items.append(item)

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)

    def list_borrowed_items(self):
        if self.borrowed_items:
            print(f"{self.name} has borrowed the following items:")
            for item in self.borrowed_items:
                print(f" - {item.display_info()}")
        else:
            print(f"{self.name} has not borrowed any items.")


class Library:
    def __init__(self):
        self.items = []
        self.users = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def register_user(self, user):
        self.users.append(user)

    def borrow_item(self, user, item):
        user.borrow(item)

    def return_item(self, user, item):
        user.return_item(item)

    def list_items(self):
        print("Library items:")
        for item in self.items:
            print(f" - {item.display_info()}")

    def list_available_items(self):
        print("Available items in the library:")
        for item in self.items:
            print(f" - {item.display_info()}")


if __name__ == "__main__":
    
    library = Library()

    
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951, 214)
    book2 = Book("1984", "George Orwell", 1949, 328)
    magazine1 = Magazine("National Geographic", "Various", 2023, 10)

   
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)

    
    user1 = LibraryUser("Alice")
    user2 = LibraryUser("Bob")

    
    library.register_user(user1)
    library.register_user(user2)

    
    library.list_available_items()

    
    library.borrow_item(user1, book1)
    library.borrow_item(user2, book2)

    
    user1.list_borrowed_items()
    user2.list_borrowed_items()

    
    library.return_item(user1, book1)

    
    library.list_available_items()

