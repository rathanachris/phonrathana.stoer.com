mongo.dbSQL
SELECT *
FROM orders
LIMIT 10;
SELECT
    customer_id,
    order_id,
    CASE
        WHEN ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date ASC, order_id ASC
        ) = 1 THEN 1
        ELSE 0
    END AS is_first_order
FROM orders;


