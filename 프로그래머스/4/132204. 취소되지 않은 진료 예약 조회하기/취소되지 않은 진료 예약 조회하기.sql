select a.apnt_no,  p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
from patient p 
join appointment a on (a.pt_no = p.pt_no)
join doctor d on (d.dr_id = a.mddr_id)
where a.apnt_ymd >= to_date('20220413','YYYYMMDD') 
and a.apnt_ymd < to_date('20220414','YYYYMMDD') 
and a.mcdp_cd = 'CS' 
and a.apnt_cncl_yn ='N' 
order by a.apnt_ymd
