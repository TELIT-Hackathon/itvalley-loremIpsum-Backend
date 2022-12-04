import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from pathlib import Path
from selects import *

app = Flask(__name__)

hi = {'hello': 'world!'}


@app.route('/')
def upload_form():
    return hi


@app.route('/messages', methods=['GET'])
def get_messages():
    args = request.args
    return get_users_messages(int(args.get("userid")))


@app.route('/messagesbyroles', methods=['GET'])
def get_m_byroles():
    args = request.args
    if args.get("getbanned") == 'False':
        return get_messages_by_users_roles(int(args.get("userid")), False)
    return get_messages_by_users_roles(int(args.get("userid")), True)


@app.route('/getuserroles', methods=['GET'])
def get_userroles():
    args = request.args
    return get_users_roles(int(args.get("userid")))


@app.route('/getmessagerole', methods=['GET'])
def get_mes_role():
    args = request.args
    return get_messages_roles(int(args.get("messageid")))


@app.route('/get_user_type', methods=['GET'])
def getusertype():
    args = request.args
    return get_messages_roles(int(args.get("type_id")))


@app.route('/get_user_by_id', methods=['GET'])
def getuserbyid():
    args = request.args
    return get_user_by_id(int(args.get("user_id")))


@app.route('/get_all_user_info', methods=['GET'])
def getallinfoaboutuser():
    args = request.args
    return get_all_info_about_user(int(args.get("user_id")))


@app.route('/get_root', methods=['GET'])
def getroot():
    return get_root_messages()


@app.route('/get_all_users', methods=['GET'])
def getusers():
    return get_all_users()

@app.route('/get_childs', methods=['GET'])
def getchilds():
    args = request.args
    return get_childs(int(args.get("message_id")))

@app.route('/change_likes', methods=['GET', 'POST'])
def changelikes():
    args = request.args
    change_likes(int(args.get("message_id")), int(args.get("n_of_likes")))
    return "OK"


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    args = request.args
    return insert_user(int(args.get("user_id")), args.get("user_type"), args.get("user_name"),
                       args.get("user_last_name"))


@app.route('/create_message', methods=['GET', 'POST'])
def create_message():
    args = request.args
    return insert_message(int(args.get("message_id")), args.get("title"), int(args.get("num_of_likes")),
                          args.get("content"), int(args.get("parrent_id")), int(args.get("author_id")),
                          int(args.get("status")))


@app.route('/create_role', methods=['GET', 'POST'])
def create_role():
    args = request.args
    return insert_role(int(args.get("role_id")), args.get("title"))


@app.route('/create_user_type', methods=['GET', 'POST'])
def create_type():
    args = request.args
    return insert_user_types(int(args.get("type_id")), args.get("user_type"))


@app.route('/create_user_roles', methods=['GET', 'POST'])
def create_user_roles():
    args = request.args
    return insert_users_roles(int(args.get("id_row")), int(args.get("role_id")), int(args.get("user_id")))


@app.route('/create_messages_roles', methods=['GET', 'POST'])
def create_messages_roles():
    args = request.args
    return insert_messages_roles(int(args.get("id_row")), int(args.get("message_id")), int(args.get("role_id")))


@app.route('/create_messages_status', methods=['GET', 'POST'])
def create_messages_status():
    args = request.args
    return insert_message_status(int(args.get("status_id")), args.get("status_name"))


@app.route('/create_banned_messages', methods=['GET', 'POST'])
def create_banned_messages():
    args = request.args
    return insert_banned_messages(int(args.get("id_row")), int(args.get("message_id")), int(args.get("user_id")))

# app.run()