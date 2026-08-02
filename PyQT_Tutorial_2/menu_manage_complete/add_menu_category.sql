USE cafe_db;

-- 기존 menus 테이블에 category 열이 없다면 한 번만 실행
ALTER TABLE menus
ADD COLUMN category VARCHAR(20) NOT NULL DEFAULT '기타'
AFTER price;

-- 기존 메뉴들의 카테고리 예시 지정
UPDATE menus
SET category = CASE
    WHEN product_name IN (
        '아메리카노',
        '카페라떼',
        '바닐라라떼',
        '카페모카',
        '카라멜마끼아또',
        '헤이즐넛라떼',
        '콜드브루',
        '콜드브루라떼',
        '에스프레소',
        '아인슈페너'
    ) THEN '커피'

    WHEN product_name IN (
        '레몬에이드',
        '자몽에이드',
        '청포도에이드',
        '복숭아아이스티'
    ) THEN '에이드'

    WHEN product_name IN (
        '아메리카노',
        '카페라떼',
        '딸기라떼',
        '망고스무디'
    ) THEN '베스트'

    ELSE '기타'
END;
