SELECT c.name, o.orderid, o.amount
FROM customers c
RIGHT JOIN orders o
	ON c.CustomerID = o.CustomerID;