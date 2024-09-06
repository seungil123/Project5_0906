def delete_book(books, book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            break
        
def read_books(books):
    for book in books:
        print(f"ID: {book['id']}, 제목: {book['title']}, 작가: {book['author']}, 대출일자: {book['date']}, 상태: {book['status']}")