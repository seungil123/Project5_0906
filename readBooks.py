from books import books_records


def read_books():
    if not books_records:
        print("도서 목록이 비어있습니다.")
    else:
        print("도서 목록 조회")
        print("="*50)
        for book in books_records:
            print(f"ID: {book['id']}, 제목: {book['title']}, 작가: {book['author']}, "
              f"상태: {book['status']}, 대출일: {book['date']}")
        print("="*50)
    