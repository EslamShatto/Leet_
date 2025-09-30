#https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/1787453770/
select emp.name as Employee 
from Employee as emp left join Employee as man on man.id = emp.managerID 
where emp.salary > man.salary