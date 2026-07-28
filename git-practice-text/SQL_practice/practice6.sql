SELECT name,
	   phone
FROM customers
WHERE SUBSTRING(phone, 1, 3) = '010'