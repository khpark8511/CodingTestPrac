select *
from (select car_id, round(avg(end_date-start_date+1),1) as average_duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
) 
where average_duration >= 7 
order by average_duration desc, car_id desc