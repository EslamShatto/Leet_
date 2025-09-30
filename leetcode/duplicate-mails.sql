#https://leetcode.com/problems/duplicate-emails/submissions/1787468773/
select  email from Person group by email having count(id) >1