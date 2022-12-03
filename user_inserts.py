import sqlite3 as sq

db_name = "database.db"

def insert_user(user_id, user_type, user_name, user_last_name):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO users (user_id, user_type, user_name, user_last_name)
    VALUES 
    (?,?,?,?)""", (user_id, user_type, user_name, user_last_name))
    con.commit()

def insert_message(message_id, title, role, num_of_likes, content, parrent_id, author_id, status):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO messages (message_id, title, role, num_of_likes, content, parrent_id, author_id, status)
    VALUES 
    (?,?,?,?,?,?,?,?)""", (message_id, title, role, num_of_likes, content, parrent_id, author_id, status))
    con.commit()

def insert_roles(role_id,title):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO roles (role_id, title)
          VALUES 
          (?,?)""", (role_id,title))
    con.commit()

def insert_user_types(type_id,user_type):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO user_types (type_id,user_type)
          VALUES 
          (?,?)""", (type_id,user_type)
    con.commit()

def insert_users_roles(id_row,role_id,user_id):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO users_roles (id_row,role_id,user_id)
          VALUES 
          (?,?,?)""", id_row,role_id,user_id)
    con.commit()

def insert_message_statuses(status_id,status_name):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO message_statuses (status_id,status_name)
          VALUES 
          (?,?)""", status_id,status_name)
    con.commit()

def insert_banned_messages(id_row,message_id,user_id):
  with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO banned_messages (id_row,message_id,user_id)
          VALUES 
          (?,?,?)""", id_row,message_id,user_id)
    con.commit()