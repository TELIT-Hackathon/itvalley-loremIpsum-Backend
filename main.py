# from hackathonDeutch import create_db, fill_db, selects
from create_db import *
from fill_db import *
from selects import *
def create_and_fill():
  create_db()
  user_types()
  roles()
  users()
  users_roles()
  message_statuses()
  messages()
  messages_roles()
  banned_messages()
  
if __name__ == "__main__":
  # create_and_fill()
  res = get_user_by_id(0)
  for i in res:
    print(i)
  print()

  res = get_user_by_id(1)
  for i in res:
    print(i)
  print()

  res = get_user_by_id(2)
  for i in res:
    print(i)
  print()

  res = get_user_by_id(3)
  for i in res:
    print(i)
  print()

  res = get_user_by_id(4)
  for i in res:
    print(i)
  print()


  res = get_all_info_about_user(4)
  for i in res:
    print(i)
  print()

  res = get_root_messages()
  for i in res:
    print(i)
  print()

  # res = get_users_roles(2)
  # for i in res:
  #   print(i)
  # print()


  # res = get_messages_by_users_roles(2, False)
  # for i in res:
  #   print(i)
  #   print()