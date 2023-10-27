select full_name, subject_name
from students
         join grades g on students.id = g.student_id
         join subjects s on s.id = g.subject_id
where students.id = 27
group by full_name, subject_name