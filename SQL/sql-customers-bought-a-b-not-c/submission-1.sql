-- Write your query below
WITH A_Product AS (
    SELECT DISTINCT product_name, customer_id
    FROM orders
    WHERE product_name = 'A'
), B_Product AS (
    SELECT DISTINCT product_name, customer_id
    FROM orders
    WHERE product_name = 'B'
), C_Product AS (
    SELECT DISTINCT product_name, customer_id
    FROM orders
    WHERE product_name = 'C'
)

SELECT DISTINCT customers.customer_id, customers.customer_name
FROM A_Product 
LEFT JOIN
B_Product
ON A_Product.customer_id = B_Product.customer_id
LEFT JOIN
C_Product
ON B_Product.customer_id = C_Product.customer_id
INNER JOIN
customers
ON A_Product.customer_id = customers.customer_id
WHERE A_Product.customer_id IS NOT NULL AND B_Product.customer_id IS NOT NULL AND C_Product.customer_id IS NULL
ORDER BY 2;