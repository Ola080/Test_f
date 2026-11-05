books: dict[str, int] = {
    "Python Basics": 3,
    "Data Science": 2,
    "Algorithms": 1,
}

borrowed_books: dict[str, int] = { }

def borrow_book(book_name: str) -> None:
    if book_name not in books:
        raise ValueError("Book not found in the library.")
    if books[book_name] <= 0:
        raise RuntimeError("No copies available for borrowing.")

    books[book_name] -= 1
    borrowed_books[book_name] = borrowed_books.get(book_name, 0) + 1
    print(f"Borrowed '{book_name}'.")

def return_book(book_name: str) -> None:
    if book_name not in borrowed_books:
        raise RuntimeError("This book was not borrowed.")

    books[book_name] += 1
    if borrowed_books[book_name] > 1:
        borrowed_books[book_name] -= 1
    else:
        del borrowed_books[book_name]

    print(f"Returned '{book_name}'.")

def test_borrow_book() -> None:
    global books, borrowed_books
    books = {"Python Basics": 3, "Data Science": 2, "Algorithms": 1}
    borrowed_books = {}

    borrow_book("Python Basics")

    assert books["Python Basics"] == 2
    assert borrowed_books == {"Python Basics": 1}


def test_borrow_book_not_found() -> None:
    global books, borrowed_books
    books = {"Python Basics": 3, "Data Science": 2, "Algorithms": 1}
    borrowed_books = {}

    with pytest.raises(ValueError, match="Book not found in the library."):
        borrow_book("Missing Book")

    assert books == {"Python Basics": 3, "Data Science": 2, "Algorithms": 1}
    assert borrowed_books == {}


def test_return_book() -> None:
    global books, borrowed_books
    books = {"Python Basics": 2, "Data Science": 2, "Algorithms": 1}
    borrowed_books = {"Python Basics": 1}

    return_book("Python Basics")

    assert books["Python Basics"] == 3
    assert borrowed_books == {}


def test_return_book_not_borrowed() -> None:
    global books, borrowed_books
    books = {"Python Basics": 3, "Data Science": 2, "Algorithms": 1}
    borrowed_books = {}

    with pytest.raises(RuntimeError, match="This book was not borrowed."):
        return_book("Python Basics")

    assert books["Python Basics"] == 3
