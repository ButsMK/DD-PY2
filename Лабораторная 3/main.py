class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = None
        self.set_pages(pages)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    def set_pages(self, pages: int):
        if isinstance(pages, int) and pages > 0:
            self.pages = pages
        elif not isinstance(pages, int):
            raise TypeError
        elif not pages > 0:
            raise ValueError


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = None
        self.set_duration(duration)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

    def set_duration(self, duration: float):
        if isinstance(duration, float) and duration > 0:
            self.duration = duration
        elif not isinstance(duration, float):
            raise TypeError
        elif not duration > 0:
            raise ValueError


if __name__ == '__main__':
    paperBook = PaperBook(name='Voina i Mir', author='Tolstoy', pages=1000)
    paperBook.set_pages(1001)
    print(paperBook)
    print(repr(paperBook))

    audioBook = AudioBook(name='Voina i Mir', author='Tolstoy', duration=1232.12)
    audioBook.set_duration(2000.23)
    print(audioBook)
    print(repr(audioBook))
