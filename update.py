from books import books_record
def update_book(books, book_id, new_date, new_status):
    for book in books:
        if book['id'] == book_id:
            book['date'] = new_date
            book['status'] = new_status
            break

          