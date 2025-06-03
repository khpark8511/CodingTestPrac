SELECT to_char(start_date,'FMMM') as month , car_id, count(*) as records
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where (start_date between to_date('20220801','YYYYMMDD') AND to_date('20221031','YYYYMMDD'))
    group by car_id
    having count(*) >=5
)
AND (start_date between to_date('20220801','YYYYMMDD') AND to_date('20221031','YYYYMMDD'))
group by to_char(start_date,'FMMM'), car_id
order by to_number(to_char(start_date,'FMMM')), car_id desc