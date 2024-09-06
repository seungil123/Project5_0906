from common import books

def update_book(book_id, borrow_date=None, is_returned=None):
      if book_id not in books:
        print("책을 찾을 수 없습니다.")
      else:
        if borrow_date is not None:
            books[book_id]['borrow_date'] = borrow_date
        if is_returned is not None:
            books[book_id]['is_returned'] = is_returned
        print(f"책 ID {book_id}의 정보가 업데이트되었습니다.")
        
if __name__ == "__main__":
    # 테스트 용도
    update_book('1', '2024-09-05', True)