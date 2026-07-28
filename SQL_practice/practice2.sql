SELECT customerid, name, age, JoinDate, City, phone
FROM customers
WHERE JoinDate >= '2024-01-01' and JoinDate <= '2025-01-01'
	and age <= 30;