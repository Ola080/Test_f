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
