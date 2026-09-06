# Write your MySQL query statement below
WITH previousData AS (
    SELECT id,recordDate,temperature,
    LAG(temperature,1) OVER (ORDER BY recordDate) AS prev_temperature,
    LAG(recordDate,1) OVER (ORDER BY recordDate) AS prev_recordDate
    FROM Weather
)

SELECT id
FROM previousData
WHERE temperature>prev_temperature AND DATEDIFF(recordDate,prev_recordDate) =1;