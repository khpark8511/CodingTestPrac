select route, 
concat(cast(round(sum(d_between_dist),1) as char), 'km') as total_distance, 
concat(cast(round(avg(d_between_dist),2) as char), 'km') as average_distance
from subway_distance
group by route
order by round(sum(d_between_dist),1) desc