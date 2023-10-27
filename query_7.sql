--Предмет з ід 2 у другої групи, змінив на виведення середньої оцінки
select students.id, full_name, avg(g.grade) as average
from students
         join grades g on students.id = g.student_id
         join groups g2 on g2.id = students.group_id
where g.subject_id = 2
  and g2.id = 2
group by students.id
order by average desc
