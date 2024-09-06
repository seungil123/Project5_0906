

for book in books:
    print(f"ID: {book['id']}, 제목: {book['title']}, 작가: {book['author']}, 대출일자: {book['date']}, 상태: {book['status']}")

# 책 추가(create)

def create_book(books, book_id, title, author, date, status):
    new_book = {"id": book_id, "title": title, "author": author, "date": date, "status": status}
    books.append(new_book)