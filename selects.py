import sqlite3 as sq

db_name = "database.db"

def get_users_messages(user_id):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM messages WHERE author_id={user_id};""")
    return [dict(row) for row in cur.fetchall()]

def get_messages_by_users_roles(user_id, get_banned=True):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    if get_banned:
      cur.execute(f"""SELECT DISTINCT messages.* FROM messages
                  INNER JOIN
                  ((SELECT role_id FROM users_roles WHERE user_id={user_id}) u_r
                  INNER JOIN 
                  messages_roles ON messages_roles.role_id=u_r.role_id) m_r
                  WHERE
                  messages.message_id=m_r.message_id;
                  """)
      return [dict(row) for row in cur.fetchall()]
    else:
      cur.execute(f"""SELECT DISTINCT messages.* FROM messages
                  INNER JOIN
                  (SELECT DISTINCT messages.message_id FROM messages
                  INNER JOIN
                  ((SELECT role_id FROM users_roles WHERE user_id={user_id}) u_r
                  INNER JOIN 
                  messages_roles ON messages_roles.role_id=u_r.role_id) m_r
                  WHERE
                  messages.message_id=m_r.message_id) tbl
                  ON messages.message_id=tbl.message_id
                  INNER JOIN banned_messages ON
                  banned_messages.user_id={user_id} AND banned_messages.message_id!=tbl.message_id;
                  """)
      return [dict(row) for row in cur.fetchall()]

def get_users_roles(user_id):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT roles.title FROM roles 
    INNER JOIN
    (SELECT role_id FROM users_roles WHERE user_id={user_id}) r 
    WHERE roles.role_id=r.role_id;""")
    return [dict(row) for row in cur.fetchall()]

def get_messages_roles(message_id):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT roles.title FROM roles 
    INNER JOIN (SELECT role_id FROM messages_roles WHERE message_id={message_id}) r 
    WHERE roles.role_id=r.role_id;""")
    return [dict(row) for row in cur.fetchall()]

############################################################################
############################################################################
def get_user_type(type_id):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT user_type FROM user_types WHERE type_id={type_id};""")
    return dict(cur.fetchone())['user_type']

def get_user_by_id(user_id):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM users WHERE user_id={user_id};""")
    return [dict(row) for row in cur.fetchall()]

def get_all_info_about_user(user_id):
  result = get_user_by_id(user_id)
  for row in result:
    row['roles'] = [i['title']for i in get_users_roles(row['user_id'])]
    row['user_type'] = get_user_type(row['user_type'])

  return result

def get_root_messages():
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM messages WHERE parrent_id='null' ORDER BY num_of_likes DESC;""")
    return [dict(row) for row in cur.fetchall()]

def get_all_users():
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM users;""")
    return [dict(row) for row in cur.fetchall()]

def change_likes(message_id, n_of_likes):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute(f"""UPDATE messages SET num_of_likes=num_of_likes+{n_of_likes}
    WHERE messages.message_id={message_id};""")

def get_childs(message_id):
  with sq.connect(db_name) as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM messages
    WHERE parrent_id={message_id};""")
    return [dict(row) for row in cur.fetchall()]
