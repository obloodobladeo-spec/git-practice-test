SELECT name AS 고객명,
	   city AS 거주지
FROM customers
WHERE SUBSTRING(city, 3, 1) = '시'
ORDER BY city ASC