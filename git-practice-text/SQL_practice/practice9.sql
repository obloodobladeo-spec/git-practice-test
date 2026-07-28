-- 그룹화 (w3schools)
SELECT c.name, o.Customerid, COUNT(amount), SUM(amount) AS 주문건수
FROM Orders as o
JOIN customers as c
ON c.customerid = o.customerid
GROUP BY o.CustomerID
HAVING SUM(amount) <= 100000