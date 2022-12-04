import sqlite3 as sq

db_name = "database.db"


def create_db():
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS user_types (
    type_id INTEGER PRIMARY KEY,
    user_type TEXT
    );""")
    con.commit()

  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS roles (
    role_id INTEGER PRIMARY KEY,
    title TEXT
    );""")
    con.commit()

  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    user_type INTEGER NOT NULL,
    user_name TEXT NOT NULL,
    user_last_name TEXT NOT NULL,
    FOREIGN KEY(user_type) REFERENCES user_types(type_id)
    );""")
    con.commit()

  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users_roles (
    id_row INTEGER PRIMARY KEY,
    role_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY(role_id) REFERENCES roles(role_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
    );""")
    con.commit()

  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS message_statuses (
    status_id INTEGER PRIMARY KEY,
    status_name TEXT
    );""")
    con.commit()

  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS messages (
    message_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    num_of_likes INTEGER DEFAULT 0,
    content TEXT,
    parrent_id INTEGER,
    author_id INTEGER,
    status INTEGER,
    FOREIGN KEY(parrent_id) REFERENCES roles(parrent_id),
    FOREIGN KEY(author_id) REFERENCES users(user_id),
    FOREIGN KEY(status) REFERENCES message_statuses(status_id)
    );""")
    con.commit()

  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS messages_roles (
    id_row INTEGER PRIMARY KEY,
    message_id INTEGER,
    role_id INTEGER,
    FOREIGN KEY(message_id) REFERENCES messages(message_id),
    FOREIGN KEY(role_id) REFERENCES roles(role_id)
    );""")
    con.commit()


  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS banned_messages (
    id_row INTEGER PRIMARY KEY,
    message_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY(message_id) REFERENCES messages(message_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
    );""")
    con.commit()


if __name__ == '__main__':
  create_db()
