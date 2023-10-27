from psycopg2 import DatabaseError
from connect import create_connection
def create_db(conn, sql):
    c = conn.cursor()
    try:
        c.execute(sql)
        conn.commit()
    except DatabaseError as e:
        print(f"Error creating database {e}")
        conn.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    with open('create_tables.sql') as f:
        sql = f.read()
    try:
        with create_connection() as conn:
            if conn is not None:
                create_db(conn, sql)
            else:
                print("Error creating")
    except RuntimeError as e:
        print(f"Error creating {e}")