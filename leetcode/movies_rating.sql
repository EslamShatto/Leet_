#https://leetcode.com/problems/movie-rating/submissions/1787516756/
(select name as results  
from MovieRating as m join Users as u on m.user_id = u.user_id  
group by results order by count(name) desc ,results asc limit 1)
UNION ALL
(select title as results 
from MovieRating as mr join Movies as m on mr.movie_id = m.movie_id 
where month(created_at) =2 and year(created_at)=2020 
group by results  order by avg(rating) desc,title asc limit 1)