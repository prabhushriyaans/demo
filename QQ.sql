SELECT CategoryName,SUM(Quantity * Price) AS
    Totalsale FROM products as p INNER JOIN categories AS
    c ON p.CategoryID=c.CategoryID INNER JOIN order_details AS od ON p.ProductID=od.ProductID GROUP BY c.CategoryID ORDER BY Totalsale DESC;