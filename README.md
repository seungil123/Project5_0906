# Project5_0906

프로젝트명: 5기 도서 대출 관리 프로그램 구현 팀원명: 조승일,이동희,김소희,이민서

프로젝트 규칙:
1.브랜치는 본인이름 이니셜 예)조승일 CSI 
2.commit 할때 수정내용 적고 복잡하면 상세하게 적기
3.branch 병합은 일괄로 팀장이 실행
4.수정하기전에 github에서 pull해오기 

## 도서 대출 관리 프로그램
###도서 목록 : 책 고유 id, 책 제목, 작가, 대출 일자, 대출 반납 상태 확인
- Create(입력) : 책 고유id, 책 제목, 작가, 대출 일자, 대출-반납 상태를
- Update(수정) : 대출 일자, 대출-반납 상태
- Delete(삭제) : 책 제목, 작가, 대출 일자, 대출-반납 상태
- Read(조회) : 도서 목록 불러오기 -> select * from <table명>

====================================================================
id  varchar(10),		/* Book ID */
title 	varchar(30),		/* Book Title */
author  varchar(20), 	/* Book's author */
status  varchar(30),  	/* Borrow status */
date  varchar(20)  	        /* Borrow Date */  
