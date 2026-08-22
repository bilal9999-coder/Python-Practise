# Practise Code of OOP Given by the Gemini To write

class Item:
    def __init__ (self, title, author):
        self.title = title
        self.author = author
    @property
    def title (self):
        return self._title
    @title.setter
    def title (self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        self._title = title
    def __str__(self):
        return f"{self.title} by {self.author}"
    __repr__ = __str__  # <--- ADD THIS LINE

class Book(Item):
    def __init__ (self, title, author, page_count):
        super().__init__(title,author)
        self.page_count = page_count

class AudioBook(Item):
    def __init__ (self, title, author, duration_minutes):
        super().__init__(title,author)
        self.duration_minutes = duration_minutes

class Library:
    inventory = []
    @classmethod
    def add_item(cls, item):
        cls.inventory.append(item)
    @classmethod
    def get_all_books(cls):
        book = []
        for things in cls.inventory:
            if isinstance(things, Book):
                book.append(things)
        return book
    @classmethod
    def from_csv_string(cls, csv_string):
        csv_string = csv_string.split(",")
        if "Book" in csv_string:
             b = Book(csv_string[1],csv_string[2],csv_string[3])
             cls.inventory.append(b)
             return b
        elif "AudioBook" in csv_string:
             a = AudioBook(csv_string[1],csv_string[2],csv_string[3])
             cls.inventory.append(a)
             return a

if __name__ == "__main__":
    # Test 1 & 2 & 3: Initialization and Validation
    b1 = Book("1984", "George Orwell", 328)
    try:
        b1.title = ""
    except ValueError as e:
        print(f"Validation works: {e}")

    # Test 4: String Representation
    print(b1)  # Should print: 1984 by George Orwell

    # Test 5: Library Manager
    Library.add_item(b1)
    Library.add_item(AudioBook("Project Hail Mary", "Andy Weir", 965))
    
    # Test 6: Factory Method
    Library.from_csv_string("Book,The Alchemist,Paulo Coelho,208")

    # Output verification
    books_only = []
    books_only= Library.get_all_books()
    print(books_only) # added that line beacuse as i am printing list from a class python use __repr__which was not defined
    print(f"Total books found: {len(books_only)}") # Should be 2 (1984, The Alchemist)