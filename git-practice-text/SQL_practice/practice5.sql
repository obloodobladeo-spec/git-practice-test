SELECT c.name,
	   c.phone,
       -- o.orderdate
       CONCAT(DATEDIFF(CURDATE(), o.orderdate), '일') AS 주문지체일
FROM Customers AS c
JOIN orders AS o
ON c.customerid = o.customerid
ORDER BY name ASC;