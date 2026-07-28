-- SQL 문법을 작성해서 실행하는 에디터
-- UTF-8
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
SET FOREIGN_KEY_CHECKS=1;

-- 손님에 대한 데이터(손님 ID, 이름, 이메일, 가입일자, 사는곳, 나이, 폰넘버)
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(150) UNIQUE NOT NULL,
    JoinDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    City VARCHAR(100),
    Age INT,
    Phone VARCHAR(20)
);

INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('박지연', 'sumin43@hotmail.com', '2024-02-03', '영월군', 41, '063-889-1065');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('오승현', 'jeongung64@ju.net', '2025-03-14', '하남시', 48, '041-086-1584');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('윤영식', 'seocaeweon@yuhanhoesa.org', '2023-10-08', '청주시 흥덕구', 36, '018-726-4785');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('고정훈', 'zgim@hanmail.net', '2024-09-11', '제천시', 46, '070-5659-9363');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('박경자', 'jongsu72@yuhanhoesa.net', '2025-06-15', '부천시 오정구', 27, '031-500-5996');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('박지영', 'jujuweon@gmail.com', '2023-10-21', '논산시', 68, '019-413-2341');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('류예진', 'kgim@jusighoesa.org', '2025-01-17', '삼척시', 50, '031-176-3314');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('손영미', 'yeongsig06@dreamwiz.com', '2024-03-17', '양구군', 44, '063-282-6042');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('홍옥순', 'sanghogang@bagangweon.com', '2024-06-23', '안산시 단원구', 66, '042-088-8710');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('윤승민', 'yejungim@jusighoesa.org', '2025-01-28', '서산시', 60, '044-081-6724');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김정웅', 'wgim@hotmail.com', '2024-09-16', '의왕시', 46, '011-419-4470');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이정수', 'gimsugja@ju.com', '2025-06-22', '보은군', 25, '063-118-1551');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김종수', 'jeonjongsu@hotmail.com', '2025-02-28', '청주시 상당구', 59, '02-5319-5144');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이영환', 'eunseogim@guica.org', '2023-10-20', '수원시 영통구', 40, '064-743-1618');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김승민', 'sujin45@nate.com', '2023-11-19', '성남시 수정구', 35, '063-755-5926');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김수빈', 'jaeho30@ibagjang.kr', '2024-03-25', '공주시', 65, '063-004-5660');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김보람', 'lgim@hanmail.net', '2025-05-13', '예산군', 61, '018-719-0007');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('박서영', 'sgo@hanmail.net', '2024-08-10', '보은군', 58, '010-4957-2867');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김지영', 'ieunyeong@daum.net', '2024-09-14', '춘천시', 38, '018-477-4045');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('박광수', 'minjaegim@ryugim.com', '2023-09-16', '남양주시', 46, '02-8117-4303');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('진민준', 'seojunbaeg@daum.net', '2023-09-19', '부천시 원미구', 70, '052-524-5728');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김진호', 'hyeonsug48@live.com', '2024-11-07', '청주시 상당구', 47, '016-831-5818');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('최영숙', 'si@imunyun.com', '2024-09-11', '성남시 분당구', 46, '052-620-6930');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('강성호', 'igwangsu@yu.com', '2024-07-16', '파주시', 44, '055-379-6422');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('송정호', 'ijeong@dreamwiz.com', '2024-05-13', '청주시 흥덕구', 49, '043-534-1030');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이지민', 'jgim@gimyang.com', '2025-01-19', '수원시 팔달구', 43, '053-861-0172');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김명자', 'gimyeongsug@daum.net', '2024-07-08', '천안시 서북구', 49, '064-767-7767');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('오재호', 'yeonggil28@daum.net', '2024-08-01', '여주시', 31, '070-2007-5356');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('안정남', 'jeongsui@naver.com', '2024-05-14', '고양시 덕양구', 18, '010-8795-1413');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이채원', 'xgim@gimgim.com', '2024-06-06', '안양시 만안구', 43, '063-431-5371');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('박순자', 'yeongsuhwang@live.com', '2024-03-09', '안양시', 39, '010-4971-8035');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('박수빈', 'gimogja@naver.com', '2025-03-11', '속초시', 69, '044-094-1478');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이은경', 'seoyeonbaeg@yuhanhoesa.kr', '2024-05-19', '수원시 권선구', 55, '032-316-6281');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('하영미', 'sunja38@yu.net', '2025-07-25', '예산군', 47, '055-332-0218');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이유진', 'sunogbag@yu.kr', '2025-03-18', '가평군', 58, '031-738-2187');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이윤서', 'minjae35@hotmail.com', '2025-02-07', '속초시', 62, '010-7092-0573');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이영숙', 'jeongungcoe@gimigim.com', '2025-06-16', '청주시 청원구', 46, '010-4278-1500');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김지우', 'icunja@yu.net', '2024-04-14', '서산시', 64, '017-038-4394');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이영희', 'yeongsunyun@ju.com', '2024-11-23', '보령시', 53, '054-035-7924');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('송영호', 'fseo@ryuisong.com', '2024-03-11', '용인시 기흥구', 38, '062-921-1067');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('배정자', 'minjungim@iyun.com', '2024-07-03', '태백시', 45, '042-323-3633');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김병철', 'jisiu@daum.net', '2024-05-15', '성남시 중원구', 45, '032-688-2178');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이은영', 'ieungyeong@live.com', '2024-03-22', '인제군', 42, '031-223-6199');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이수빈', 'bagjihu@ju.net', '2025-04-11', '화천군', 49, '054-138-5498');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('이유진', 'eunjeong86@live.com', '2024-01-07', '속초시', 25, '042-176-5493');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김현주', 'nhong@dreamwiz.com', '2023-10-23', '인제군', 38, '011-925-4977');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('장영숙', 'yeongmi43@igim.com', '2025-07-23', '양구군', 39, '018-737-1761');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('전영호', 'seunghyeon12@dreamwiz.com', '2024-01-28', '수원시 장안구', 20, '010-5850-1046');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('김은경', 'cunjacoe@hanmail.net', '2024-03-14', '안양시 만안구', 38, '033-423-9568');
INSERT INTO Customers (Name, Email, JoinDate, City, Age, Phone) VALUES ('최정식', 'ogsun84@dreamwiz.com', '2024-03-13', '평택시', 41, '053-801-1918');

-- 손님의 주문 데이터(주문ID, 손님ID, 주문내역, )
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT, -- AUTO_INCREMENT: 자동 증가(할당)
    CustomerID INT,
    OrderDate DATE,
    Amount INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);    -- 테이블 끼리 커스터머 아이디로 연결이 되어있다. (관계형 데이터 베이스)

INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (34, '2025-04-09', 196363);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (18, '2025-05-10', 39435);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (17, '2024-09-20', 182992);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (20, '2025-02-12', 159253);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (30, '2025-05-16', 171910);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (23, '2024-11-10', 89254);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (31, '2024-09-07', 194016);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (27, '2025-08-10', 185927);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (40, '2024-09-20', 89793);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (36, '2025-01-08', 153872);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (10, '2024-10-31', 35438);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (15, '2024-08-30', 67917);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (22, '2024-09-03', 14340);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (26, '2024-11-27', 80890);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (46, '2024-10-15', 124344);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (44, '2025-07-08', 118166);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (38, '2025-05-01', 58521);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (6, '2025-04-12', 25899);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (50, '2025-02-13', 168724);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (24, '2025-04-21', 87054);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (41, '2025-04-27', 33005);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (43, '2025-07-30', 2386);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (2, '2024-09-25', 174618);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (2, '2025-03-19', 150585);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (29, '2025-02-21', 134093);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (37, '2024-08-21', 154179);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (17, '2024-11-11', 140716);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (42, '2025-03-28', 1396);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (18, '2024-11-15', 143186);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (21, '2024-10-02', 55386);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (11, '2025-02-09', 133731);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (8, '2024-10-01', 39786);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (50, '2025-08-02', 198006);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (44, '2025-08-09', 169518);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (41, '2024-08-21', 132042);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (21, '2025-04-20', 101890);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (32, '2025-07-16', 180481);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (15, '2024-09-23', 35582);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (16, '2025-01-11', 101621);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (47, '2025-07-05', 43431);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (18, '2025-04-10', 8116);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (40, '2025-06-02', 82888);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (22, '2025-06-05', 9910);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (2, '2025-01-06', 142221);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (8, '2024-09-02', 172094);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (43, '2025-04-19', 158961);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (24, '2024-11-17', 48894);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (50, '2025-06-29', 127843);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (31, '2025-04-20', 34683);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (38, '2025-08-03', 133826);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (42, '2025-06-11', 25470);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (27, '2024-10-19', 86108);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (41, '2024-12-16', 152033);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (26, '2025-06-27', 40255);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (13, '2025-05-27', 15387);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (45, '2025-08-10', 39223);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (38, '2025-04-17', 106286);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (12, '2025-01-04', 130278);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (35, '2024-10-26', 141979);
INSERT INTO Orders (CustomerID, OrderDate, Amount) VALUES (15, '2025-04-09', 194481);