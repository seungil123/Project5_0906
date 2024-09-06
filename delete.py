from books import books_records
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
