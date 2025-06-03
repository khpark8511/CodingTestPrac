select to_char(sales_date,'YYYY') as YEAR , to_char(sales_date,'FMMM') as MONTH , a.gender as GENDER, COUNT(distinct b.user_id) AS USERS 
from user_info a 
join online_sale b on (a.user_id = b.user_id)
where a.gender is not null
group by to_char(sales_date,'YYYY'), to_char(sales_date,'FMMM'), a.gender
order by to_char(sales_date,'YYYY'), to_number(to_char(sales_date,'FMMM')), a.gender