import logging

import faker
from random import randint

from psycopg2 import DatabaseError
import psycopg2

from connect import create_connection

NUMBER_OF_GROUPS = 3
NUMBER_OF_STUDENTS = 40
NUMBER_OF_SUBJECTS = 8
NUMBER_OF_TEACHERS = 4
NUMBER_OF_GRADES = 20


def generate_fake_data(n_groups, n_students, n_subjects, n_teachers, n_grades):
    groups = []
    students = []  # contains fake students' names
    date_of_birth = []  # contains fake date of birth
    subjects = ['Mathematics', 'History', 'Computer Science', 'Biology', 'Chemistry', 'Literature', 'Physics',
                'Geography']
    teachers = []  # contains fake teachers' names
    grades = []  # contains fake grades and its dates
    dates_this_month = []
    data = faker.Faker()

    for i in range(n_groups):
        groups.append(chr(65 + i))

    for i in range(n_students):
        students.append(data.name())
        date_of_birth.append(data.date_of_birth())

    for i in range(n_teachers):
        teachers.append(data.name())

    for i in range(n_students):
        for j in range(n_subjects):
            for k in range(n_grades):
                grades.append(randint(0, 100))
                dates_this_month.append(data.date_this_month())

    return teachers, groups, students, subjects, grades, date_of_birth, dates_this_month


def prepare_data(teachers, groups, students, subjects, grades, date_of_birth, dates_this_month):
    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_groups = []
    for group in groups:
        for_groups.append((group,))

    for_students = []
    for i in range(len(students)):
        for_students.append((students[i], date_of_birth[i], (i % 3)+1))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, len(teachers))))

    for_grades = []
    grade_iterator = 0
    for subject in range(1, len(subjects) + 1):
        for student in range(1, len(students) + 1):
            for i in range(NUMBER_OF_GRADES):
                for_grades.append((student, subject, grades[grade_iterator], dates_this_month[grade_iterator]))
                grade_iterator += 1

    return for_teachers, for_groups, for_students, for_subjects, for_grades


def insert_data(teachers, groups, students, subjects, grades):
    try:
        with create_connection() as conn:
            if conn is not None:
                try:
                    c = conn.cursor()
                    sql_teachers = """INSERT INTO teachers(full_name) values (%s)"""
                    for teacher in teachers:
                        c.execute(sql_teachers, teacher)

                    sql_groups = """INSERT INTO groups(name) values (%s)"""
                    for group in groups:
                        c.execute(sql_groups, group)

                    sql_students = """INSERT INTO students(full_name, date_of_birth, group_id) values (%s,%s,%s)"""
                    for student in students:
                        c.execute(sql_students, student)

                    sql_subjects = """INSERT INTO subjects(subject_name, teacher_id) values (%s,%s)"""
                    for subject in subjects:
                        c.execute(sql_subjects, subject)

                    sql_grades = """INSERT INTO grades(student_id, subject_id, grade, date_received) values (%s,%s,%s,%s)"""
                    for grade in grades:
                        c.execute(sql_grades, grade)
                    conn.commit()
                except DatabaseError as e:
                    logging.error(e)
                    conn.rollback()
                finally:
                    c.close()
    except RuntimeError as e:
        logging.error(e)


if __name__ == '__main__':
    teachers, groups, students, subject, grades, d_birth, d_month = generate_fake_data(NUMBER_OF_GROUPS,
                                                                                      NUMBER_OF_STUDENTS,
                                                                                      NUMBER_OF_SUBJECTS,
                                                                                      NUMBER_OF_TEACHERS,
                                                                                      NUMBER_OF_GRADES)

    teachers, groups, students, subject, grades = prepare_data(teachers, groups, students, subject, grades, d_birth,
                                                              d_month)

    insert_data(teachers, groups, students, subject, grades)
