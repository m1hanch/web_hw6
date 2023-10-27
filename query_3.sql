select g.name, avg(grade)
from grades
         join students s on s.id = grades.student_id
         join groups g on g.id = s.group_id
where subject_id = 4
group by g.name