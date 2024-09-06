import books
def delete_book(books, book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
          