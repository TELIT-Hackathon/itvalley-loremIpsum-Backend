import sqlite3 as sq

db_name = "database.db"


def get_users_messages(user_id):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM messages WHERE author_id={user_id};""")
    return [dict(row) for row in cur.fetchall()]
