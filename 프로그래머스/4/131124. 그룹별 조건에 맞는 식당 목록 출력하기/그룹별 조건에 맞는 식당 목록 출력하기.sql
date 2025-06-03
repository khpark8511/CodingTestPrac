select b.member_name, a.review_text, to_char(a.review_date,'YYYY-MM-DD') as review_date
from (
    select * 
    from rest_review 
    where member_id in (
        select member_id
        from (select member_id, count(*) as cnt 
                from rest_review
            group by member_id) 
        where cnt = (select max(count(*)) as cnt from rest_review group by member_id))
) a join member_profile b on (a.member_id = b.member_id)
order by review_date, review_text 