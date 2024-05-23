import sqlite3

from core.repositories.database_module.setup_database import software_database


def execute_query(query: str, values=None):
    result = None

    conn = sqlite3.connect(software_database)
    cur = conn.cursor()

    cur.execute("BEGIN TRANSACTION")
    try:
        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)

        if query.find("SELECT") >= 0:
            result = cur.fetchall()
        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        raise e

    conn.commit()
    conn.close()

    return result
