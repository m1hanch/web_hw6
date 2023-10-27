select full_name, avg(g.grade)
from teachers
         join subjects s on teachers.id = s.teacher_id
         join grades g on s.id = g.subject_id
group by full_name