select full_name, s.subject_name
from teachers
         join subjects s on teachers.id = s.teacher_id
where teacher_id = 4