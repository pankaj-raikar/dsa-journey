# Write your MySQL query statement below
WITH Consec AS(
SELECT *, LEAD(num,1) OVER() AS nextNum,LEAD(num,2) OVER() AS next2nextNum
FROM Logs)

SELECT DISTINCT num AS ConsecutiveNums
FROM Consec
WHERE num=nextNum AND num = next2nextNum