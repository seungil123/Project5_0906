from common import books

def update_book(book_id, borrow_date=None, is_returned=None):
      if book_id not in books:
        print("책을 찾을 수 없습니다.")
      else:
        if borrow_date is not None:
            books[book_id]['borrow_date'] = borrow_date