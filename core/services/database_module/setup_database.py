import sqlite3

software_database: str = 'test.db'


def setup_database(directory) -> None:
    conn = sqlite3.connect(directory.__str__() + software_database)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student
        (
            id char(32) primary key,
            name varchar(30) not null,
            last_name varchar(30) not null,
            submitted_works_count integer not null default 0
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS work
        (
            id char(32) primary key, 
            student_id char(32) not null, 
            foreign key(student_id) references student(id) on delete cascade, 
            submitting_date datetime default current_timestamp, 
            file varchar(100), 
            mark_date datetime, 
            mark integer
        )
    """)

    conn.commit()
    conn.close()
