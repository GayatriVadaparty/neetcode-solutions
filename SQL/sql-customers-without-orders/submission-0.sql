-- Write your query below
select distinct name from customers c 
where id not in (select customer_id from orders ) 