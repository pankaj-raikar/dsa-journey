# Write your MySQL query statement below
SELECT cat.category,COUNT(T.category) as accounts_count
FROM (select 'Low Salary' as category UNION SELECT 'Average Salary' UNION SELECT 'High Salary') cat
left join
(SELECT *,case when income < 20000 then 'Low Salary'
WHEN income BETWEEN 20000 and 50000 then 'Average Salary'
ELSE 'High Salary' END as category
FROM accounts) T
on cat.category = T.category
group by cat.category
