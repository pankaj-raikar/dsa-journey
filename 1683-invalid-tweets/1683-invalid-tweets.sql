# Write your MySQL query statement below
SELECT TWEET_ID
FROM Tweets
WHERE CHAR_LENGTH(CONTENT) > 15