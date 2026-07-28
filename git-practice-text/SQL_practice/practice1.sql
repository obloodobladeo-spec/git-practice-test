SELECT name, city, JoinDate
FROM customers 
WHERE '2026-01-01' >= JoinDate and JoinDate >= '2022-01-01';
-- 키워드는 소문자 대문자 아무거나 써도 무관, 다만 하나로 통일해주는 것이 나음
-- row나 column 값도 대소문자가 바뀌어도 무관(대소문자만 다르고 문자는 같은 데이터는?)