from readBooks import read_books
from delete import delete_book_by_user_input
from update import update_book
from createBooks import create_book

while True:
    print("================================================")
    print("              도서 대출 관리 프로그램              ")
    print("환영합니다. 이용하실 서비스의 번호를 입력해주십시오.")
    print("              1. 도서 목록 조회")
    print("              2. 도서 목록 추가")
    print("              3. 도서 목록 삭제")
    print("              4. 도서 목록 수정")
    print("              5.     종료")
    print("================================================")
    T = input("                 입력 : ")
    if T=='1':
        read_books()
    elif T=='2':
        create_book()
    elif T=='3':
        delete_book_by_user_input()
    elif T=='4':
        update_book()
    elif T=='5':
        break
    else:
        print("입력이 잘못되었습니다.")
        continue