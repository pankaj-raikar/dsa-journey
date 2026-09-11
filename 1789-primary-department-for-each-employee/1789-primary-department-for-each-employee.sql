# Write your MySQL query statement below

select e.employee_id,e.department_id
from Employee e
left join 
(SELECT employee_id,COUNT(department_id) AS num_dept
FROM Employee
GROUP BY employee_id) t
ON e.employee_id=t.employee_id
where t.num_dept=1 or (num_dept>1 and primary_flag="Y")