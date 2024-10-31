class Book:
    def __init__(self, title, author, isbn, available) -> None:
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = available

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_available(self):
        return self.__available
    
    def borrow(self):
        self.__available = False

    def return_book(self):
        self.__available = True

    def is_available(self):
        return self.__available
    

class Person:
    def __init__(self, name, id_number) -> None:
        self.__name = name
        self.__id_number = id_number

    def get_info(self):
        return f'name: {self.__name}, id number: {self.__id_number}'
    

class Reader(Person):
    def __init__(self, name, id_number) -> None:
        super().__init__(name, id_number)
        self.__borrowed_books = []

    def borrow_book(self, book: Book):
        if book.is_available():
            self.__borrowed_books.append(book)
            book.borrow()
            print(f'book {book.get_title()} borrowed')
        else:
            print(f'{book.get_title()} is not available')

    def return_book(self, book: Book):
        self.__borrowed_books.remove(book)
        book.return_book()


class Librarian(Person):
    def __init__(self, name, id_number) -> None:
        super().__init__(name, id_number)

    @staticmethod
    def check_availability(book: Book):
        return book.is_available()
    
b1 = Book('title b1', 'autnor b1', 'b1 123456', True)
b2 = Book('title b2', 'autnor b2', 'b2 123456', True)
l = Librarian('Librarian name', '123456')
r = Reader('Reader name', 123456)

print(l.check_availability(b1))
print(l.check_availability(b2))

r.borrow_book(b1)
r.borrow_book(b1)

print(l.check_availability(b1))

r.return_book(b1)
print(l.check_availability(b1))
