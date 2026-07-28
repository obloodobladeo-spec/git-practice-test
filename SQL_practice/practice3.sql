CREATE TABLE Friends
(
	PersonID INT PRIMARY KEY AUTO_INCREMENT,
	Name VARCHAR(50) NOT NULL,
    City VARCHAR(20),
    Phone VARCHAR(50),
    Money INT
);

INSERT INTO Friends (Name, City , Phone, Money) 
VALUES ('구범주', '전남 화순읍 힐스테이트', '010-5877-4485', 10000000);
INSERT INTO Friends (Name, City, Phone, Money) 
VALUES 
('유재혁', '전남 화순읍 산이고운 아파트', '010-1234-5678', 50000000),
('김정권', '전남 화순읍 노대길 주택', '010-1234-5678', 50000000);

-- 단일 행 입력
INSERT INTO Friends (Name, City, Phone, Money)
VALUES ('홍길동', '서울시', '010-1234-5678', 10000000);
INSERT INTO Friends (Name, City, Phone, Money)
VALUES ('홍길동', '서울시', '010-1234-5678', 10000000);

-- 열 지정 생략(모든 열에 값 입력)(알아서 테이블의 열 값에 따라 입력)
INSERT INTO Friends
VALUES (6, '김철수', '대전시', '010-1234-5678', 20000000);

-- 여러 행 한번에 입력
INSERT INTO Friends (Name, City, Phone, Money)
VALUES 
	('이영희', '광주시', '010-1234-5678', 50000000),
    ('박민수', '순천시', '010-1234-5678', 80000000);