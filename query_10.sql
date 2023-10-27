select students.full_name as student, subject_name as subject, t.full_name as teacher
from students
         join grades g on students.id = g.student_id
         join subjects s on s.id = g.subject_id
         join teachers t on t.id = s.teacher_id
where students.id = 17
  and teacher_id = 4
group by students.full_name, subject_name, t.full_name