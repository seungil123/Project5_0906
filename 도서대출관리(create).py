# 도서 추가 (Create)
def create_book(books):
    book_id = input("책 ID를 입력하세요: ")
    title = input("책 제목을 입력하세요: ")
    author = input("작가를 입력하세요: ")
    date = input("대출 일자를 입력하세요 (YYYY-MM-DD): ")
    status = input("대출 상태를 입력하세요 (대출 중/반납 완료): ")
    
    new_book = {"id": book_id, "title": title, "author": author, "date": date, "status": status}
    books.append(new_book)
    print(f"책 '{title}'이(가) 추가되었습니다.")
    