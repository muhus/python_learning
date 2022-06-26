from datetime import datetime


class Library:
    def __init__(self, name: str, books: set, authors: set):
        self.name = name
        self.books = books
        self.authors = authors


class Book:
    def __init__(self, name: str, year: int, author: object):
        self.name = name
        self.year = year
        self.author = author
        self.validate_author()
        self.validate_year()

    def validate_author(self):
        if not isinstance(self.author, Author):
            raise ValueError("author must be instance of Author class")

    def validate_year(self):
        if not 0 <= int(self.year) <= 2022:
            raise ValueError("year must be in 0 - 2022")


class Author:
    def __init__(self, name: str, country: str, birthday: datetime, books: set):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books


# print(datetime.now())
test_obj = Author('sadf', 'selo', '2022-04-02 17:32:14.425446', ['sdfasf'])
test = Book('name', 1890, test_obj)

print(test_obj.__class__.__mro__)
