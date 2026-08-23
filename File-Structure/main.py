from Packages import book,student

if __name__ == "__main__":
    b = book.Book("GoT","GRRM")
    print(b)
    book.hello("Bilal")
    print(book.B1)
    s = student.Student("Bilal","CS")
    print(s.sort())
    print(f"{__name__}")
