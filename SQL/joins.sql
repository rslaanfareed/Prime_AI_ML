CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700)


select * from customers;
select * from orders;

-- inner join

select c.customer_id, c.name, o.order_id from customers c
inner join orders o
on c.customer_id=o.customer_id;


-- left join

select c.customer_id, c.name, o.order_id from customers c
left join orders o
on c.customer_id=o.customer_id;


-- right join

select c.customer_id, c.name, o.order_id from customers c
right join orders o
on c.customer_id=o.customer_id;


-- outer join - (left join union right join)

SELECT c.customer_id, c.name, o.order_id FROM customers as c
LEFT JOIN orders as o
ON c.customer_id = o.customer_id
UNION
SELECT c.customer_id, c.name, o.order_id FROM customers as c
RIGHT JOIN orders as o
ON c.customer_id = o.customer_id;



-- cross join

select * from customers
cross join orders;


-- self join

SELECT *
FROM customers as A
JOIN customers as B
ON A.customer_id = B.customer_id;


-- left exclusive join

SELECT *
FROM customers as A
LEFT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE B.customer_id IS NULL;



-- right exclusive join

SELECT *
FROM customers as A
RIGHT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE A.customer_id IS NULL;