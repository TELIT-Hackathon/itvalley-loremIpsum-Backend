import csv
from user_inserts import *



def user_types():
  with open("db_default/user_types.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for type_id, user_type in rows:
      insert_user_types(type_id, user_type)


def roles():
  with open("db_default/roles.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for role_id, title in rows:
      insert_role(role_id, title)

def users():
  with open("db_default/users.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for user_id, user_type, user_name, user_last_name in rows:
      insert_user(user_id, user_type, user_name, user_last_name)


def users_roles():
  with open("db_default/users_roles.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for id_row,role_id,user_id in rows:
      insert_users_roles(id_row,role_id,user_id)

def message_statuses():
  with open("db_default/message_statuses.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for status_id, status_name in rows:
      insert_message_status(status_id, status_name)

def messages():
  with open("db_default/messages.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for message_id, title, num_of_likes, content, parrent_id, author_id, status in rows:
      insert_message(message_id, title, num_of_likes, content, parrent_id, author_id, status)

def messages_roles():
  with open("db_default/messages_roles.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for id_row,message_id,role_id in rows:
      insert_messages_roles(id_row,message_id,role_id)


def banned_messages():
  with open("db_default/banned_messages.csv", "r", encoding="utf-8") as fr:
    rows = csv.reader(fr, delimiter=',')
    
    for id_row,message_id,user_id in rows:
      insert_banned_messages(id_row,message_id,user_id)

if __name__ == '__main__':
  pass