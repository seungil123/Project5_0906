# 도서목록
books_record = [{"id": "001", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "date": "2024-09-06", "status": "대출 중"},
    {"id": "002", "title": "1984", "author": "George Orwell", "date": "2024-08-20", "status": "반납 완료"},
    {"id": "003", "title": "To Kill a Mockingbird", "author": "Harper Lee", "date": "2024-09-01", "status": "대출 중"}]

# 작가 이름 또는 책 제목을 기준으로 도서를 삭제하는 함수
def delete_book_by_user_input(books):
    user_input = input("삭제할 책 제목 또는 작가 이름을 입력하세요: ")
    to_delete = None
    for book in books:
        if book['title'].lower() == user_input.lower() or book['author'].lower() == user_input.lower():
            to_delete = book
            break
    
    if to_delete:
        books.remove(to_delete)
        print(f"도서 '{to_delete['title']}' (작가: {to_delete['author']})가 삭제되었습니다.")
    else:
        print("해당하는 도서를 찾을 수 없습니다.")
