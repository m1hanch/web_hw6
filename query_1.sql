select students.id, full_name, avg(g.grade) as average
from students
         join grades g on students.id = g.student_id
group by students.id
order by average desc
limit 5