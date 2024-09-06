from books_records import books


def read_books():
    print("도서 목록 조회")
    print("="*50)
    for book in books:
        print(f"ID: {book['id']}, 제목: {book['title']}, 작가: {book['author']}, "
              f"상태: {book['status']}, 대출일: {book['date']}")
    print("="*50)
    