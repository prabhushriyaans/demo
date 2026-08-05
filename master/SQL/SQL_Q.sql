SELECT ProductName,SUM(Quantity * Price) AS
    Totalsale FROM products as p INNER JOIN order_details AS od ON p.ProductID=od.ProductID GROUP BY p.ProductID ORDER BY Totalsale DESC LIMIT 3;