# Write your MySQL query statement below

SELECT ROUND(COUNT(DISTINCT f.player_id)/COUNT(DISTINCT a.player_id),2) AS fraction
FROM Activity a
LEFT JOIN
(SELECT player_id,MIN(event_date) AS FD
FROM Activity
GROUP BY player_id) f
ON a.player_id=f.player_id AND
DATE_SUB(a.event_date,INTERVAL 1 DAY) = f.FD