import sqlite3

software_database: str = 'db.sqlite3'


def setup_database(directory: str) -> None:
    print("Creating database")
    conn = sqlite3.connect(directory.__str__() + "/" + software_database)
    cur = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS software
        (
            name char(100) primary key,
            version varchar(10) not null,
            description text not null,
            license_number char(30) not null,
            developer_company char(30) not null
        )
    """
    cur.execute(query)
    conn.commit()
    print("Created database")
    cur.execute("SELECT * FROM software;")
    conn.commit()
    conn.close()
