select grades.id, grade from grades
                 join students s on s.id = grades.student_id
                 join groups g on s.group_id = g.id
where date_received = (select max(date_received) from grades) and g.id = 3

