from books import books_record

def update_book(books, book_id, new_date, new_status):
    for book in books:
        if book['id'] == book_id:
            book['date'] = new_date
            book['status'] = new_status
            print(f"ID가 {book_id}인 책이 성공적으로 업데이트되었습니다.")
            return
    print(f"ID가 {book_id}인 책을 찾을 수 없습니다.")

def get_user_input():
    try:
        book_id = int(input("책 ID를 입력하세요: "))
        new_date = input("새로운 날짜를 입력하세요 (YYYY-MM-DD): ")
        new_status = input("새로운 상태를 입력하세요: ")
        
        if not new_date or not new_status:
            raise ValueError("날짜와 상태는 비워둘 수 없습니다.")
        
        return book_id, new_date, new_status
    except ValueError as e:
        print(f"잘못된 입력: {e}")
        return None, None, None

def main():
    book_id, new_date, new_status = get_user_input()
    if book_id is not None:
        update_book(books_record, book_id, new_date, new_status)

if __name__ == "__main__":
    main()