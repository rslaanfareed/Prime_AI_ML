CREATE VIEW view1 AS
SELECT customer_id, name FROM customers;

select * from view1;

CREATE VIEW view2 AS
SELECT c.customer_id, c.name, o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

select * from view2;

Drop view view1;