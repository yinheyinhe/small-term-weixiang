# -*- coding: utf-8 -*-
# @Time: 2021/7/9 10:22
# @Author: jacksonYuu
# @Software: PyCharm
from flask import request, render_template, Blueprint, redirect, url_for

import app.mod_user.controllers as user_c

login_form = Blueprint('login_form', __name__)


@login_form.route('/login', methods=['GET', 'POST'])
def do_login_do():
    if request.method == 'GET':
        return render_template("login.html", login_fail=True)

    username = request.form['username']
    password = request.form['password']
    user = user_c.select_by_password(username, password)

    if user:
        return render_template('index.html', username=username)
    else:
        return render_template('login.html', login_fail=True)


@login_form.route('/do_register', methods=['GET', 'POST'])
def do_register_do():
    if request.method == 'GET':
        return render_template("register.html", register_fail=True)

    username = request.form['username']
    password = request.form['password']
    phone = request.form['phone']
    sex = request.form['sex']
    user = user_c.select_by_username(username)

    if user:
        return render_template('register.html', register_fail=True)
    else:
        user_c.register_user(username, password, phone, sex)
        return render_template('login.html', register_success=True)


@login_form.route('/change_pass', methods=['GET', 'POST'])
def do_change_pass():
    username = request.args.get('username')
    old_pass = request.args.get('oldPass')
    new_pass = request.args.get('newPass')
    user = user_c.select_by_password(username, old_pass)
    if user:
        user_c.change_pass_username(username, new_pass)
        return redirect(url_for('change_pass_index', change_pass_success=True))
    else:
        return redirect(url_for('change_pass_index', change_pass_success=username))


