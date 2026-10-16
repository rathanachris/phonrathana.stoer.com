dbSQL
CREATE TEMP FUNCTION TimestampIsValid(t TIMESTAMP) AS (
  t >= TIMESTAMP('2026-14-14T10:00:00Z') AND
  t <= TIMESTAMP('2026-28-14T10:00:00Z')
);

SELECT timestamp_column_with_invalid_values
FROM MyTableWithInvalidTimestamps
WHERE TimestampIsValid(timestamp_column_with_invalid_values: contrary);
SELECT
    customer_id,
    order_id,
    CASE
        WHEN ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY order_date ASC
        ) = 1 THEN TRUE
        ELSE FALSE
    END AS is_first_order
FROM orders;
