class Book:
    page_material = 'paper'
    text = True

    def __init__(self, title, author, page_count, isbn, reserved: bool):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        return (
            f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, материал: {Book.page_material}"
            + (", зарезервирована" if self.reserved else "")
        )


books = [
    Book('The Great Gatsby', 'F. Scott Fitzgerald', 180, '9780743273565', False),
    Book('Brave New World', 'Aldous Huxley', 268, '9780060850524', False),
    Book('The Old Man and the Sea', 'Ernest Hemingway', 128, '9780684830490', False),
    Book('For Whom the Bell Tolls', 'Ernest Hemingway', 480, '9780684830490', False),
    Book('The Master and Margarita', 'Mikhail Bulgakov', 384, '9780143108269', True),
]

for book in books:
    print(book)


class SchoolBooks(Book):  # Добавлена дополнительная пустая строка перед этим классом
    def __init__(self, title, author, page_count, isbn, reserved: bool, subject, class_room, exercise: bool):
        super().__init__(title, author, page_count, isbn, reserved)
        self.subject = subject
        self.class_room = class_room
        self.exercise = exercise

    def __str__(self):
        base = (
            f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
            f"предмет: {self.subject}, класс: {self.class_room}"
        )
        return base + (", зарезервирована" if self.reserved else "")


school_books = [
    SchoolBooks('Алгебра', 'А. Н. Иванов', 200, '223-ISBN', False, 'Математика', 9, True),
    SchoolBooks('История', 'Б. Н. Сидорова', 300, '234-ISBN', False, 'История', 11, True),
    SchoolBooks('Биология', 'С. Н. Петров', 250, '331-ISBN', True, 'Биология', 8, True),
]

for book in school_books:
    print(book)