class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if self.books:
            return self.books[-1].id + 1
        else:
            return 1

    def get_index_by_book_id(self, id: int):
        exist_flag = False
        for i, book  in enumerate(self.books):
            if book.id == id:
                exist_flag = True
                return i
        if not exist_flag:
            raise ValueError("Книги с запрашиваемым id не существует")

