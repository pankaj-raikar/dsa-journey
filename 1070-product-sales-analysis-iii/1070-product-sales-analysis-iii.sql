# Write your MySQL query statement below
SELECT product_id,YEAR AS first_year,quantity,price
FROM Sales
WHERE (product_id,year) IN
(select product_id, MIN(year)
FROM Sales
group by product_id)
