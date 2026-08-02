실행 순서

1. MySQL Workbench에서 add_menu_category.sql 실행
   - 이미 menus 테이블에 category 열이 있다면 ALTER TABLE 부분은 실행하지 마세요.

2. 필요한 패키지 설치
   pip install PyQt5 pymysql

3. db_helper.py의 DB_CONFIG 비밀번호 확인

4. 실행
   python menu_manage.py

구현 기능
- 카테고리별 메뉴 조회
- 메뉴 카드 4열 동적 배치
- 마지막 메뉴 다음 칸에 메뉴 추가 버튼 배치
- 메뉴 추가 후 추가 버튼 자동 이동
- 메뉴 카드 클릭 시 수정 창 열기
- 메뉴명, 가격, 카테고리 수정
- 메뉴 삭제
- 메뉴가 많아지면 세로 스크롤
