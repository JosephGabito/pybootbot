class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.book.append(book)

    def remove_book(self, book):
        if self.title == book.title and self.author == book.author:
            self.book.remove(book)

    def search_books(self, search_string):
        search_result_list = []
        for book in self.books:
            if search_string in book.title or search_string in book.author:
                search_result_list.append(book)
        return search_result_list
