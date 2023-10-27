select t.full_name as teacher, s.full_name as student, avg(grade) as average
from grades
         join students s on s.id = grades.student_id
         join subjects s2 on s2.id = grades.subject_id
         join teachers t on t.id = s2.teacher_id
where t.id = 4
  and s.id = 31
group by t.full_name, s.full_name