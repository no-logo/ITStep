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
    
