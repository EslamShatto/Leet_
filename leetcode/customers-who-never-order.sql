#https://leetcode.com/problems/customers-who-never-order/submissions/1787474986/
select name as customers from Customers left join Orders on Customers.id = Orders.customerId where Orders.id is NULL