# -*- coding: utf-8 -*-
# @Time: 2021/7/8 21:42
# @Author: jacksonYuu
# @Software: PyCharm
import os
import threading
import time

from flask import render_template, request, redirect, url_for

from app import app, socketio
from app.mod_auth.forms import login_form
from app.mod_employee.views import employee_view
from app.mod_oldperson.views import oldperson_view
from app.mod_user.views import user_view
from app.mod_volunteer.views import volunteer_view
import app.mod_oldperson.controllers as oldperson_c
import app.mod_employee.controllers as employee_c
import app.mod_volunteer.controllers as volunteer_c

app.register_blueprint(login_form)
app.register_blueprint(oldperson_view)
app.register_blueprint(user_view)
app.register_blueprint(employee_view)
app.register_blueprint(volunteer_view)


# 访问/目录跳转到login.html页面
@app.route('/')
def login():
    return render_template("login.html")


# 访问/register目录跳转到register.html页面
@app.route('/register')
def register():
    return render_template("register.html")


# 访问/index目录跳转到index.html页面
@app.route('/index/<string:username>')
def index(username):
    if username:
        return render_template("index.html", username=username)
    else:
        return render_template("login.html", login_no=True)


# 访问/目录跳转到login.html页面
@app.route('/change_pass_success/<string:change_pass_success>')
def change_pass_index(change_pass_success):
    if change_pass_success == 'True':
        return render_template("login.html", change_pass_success=change_pass_success)
    else:
        return render_template("index.html", change_pass_success=change_pass_success, username=change_pass_success)


# 访问/member_list目录跳转到member-list.html页面
@app.route('/member_list')
def member_list():
    return render_template('member-list.html')


# 访问/member_detail目录跳转到member-detail.html页面
@app.route('/member_detail')
def member_detail():
    user_id = request.args.get('id')
    return render_template('member-detail.html', user_id=user_id)


# 访问/member_add目录跳转到member-add.html页面
@app.route('/member_add')
def member_add():
    return render_template('member-add.html')


# 访问/member_edit目录跳转到member-edit.html页面
@app.route('/member_edit')
def member_edit():
    user_id = request.args.get('id')
    return render_template('member-edit.html', user_id=user_id)


# 访问/oldperson_list目录跳转到oldperson-list.html页面
@app.route('/oldperson_list')
def oldperson_list():
    return render_template('oldperson-list.html')


# 访问/oldperson_detail目录跳转到oldperson-detail.html页面
@app.route('/oldperson_detail')
def oldperson_detail():
    user_id = request.args.get('id')
    return render_template('oldperson-detail.html', user_id=user_id)


# 访问/oldperson_add目录跳转到oldperson-add.html页面
@app.route('/oldperson_add')
def oldperson_add():
    return render_template('oldperson-add.html')


# 访问/oldperson_edit目录跳转到oldperson-edit.html页面
@app.route('/oldperson_edit')
def oldperson_edit():
    user_id = request.args.get('id')
    return render_template('oldperson-edit.html', user_id=user_id)


# 访问/oldperson_charts目录跳转到oldperson-charts.html页面
@app.route('/oldperson_charts')
def oldperson_charts():
    # main1_list = [30, 20, 36, 10, 8, 5]
    main2_list = [30, 20, 36, 10, 8, 18]
    main1_list = oldperson_c.select_oldperson_by_age()
    return render_template('oldperson-charts.html', main1_list=main1_list, main2_list=main2_list)


# 访问/employee_list目录跳转到employee-list.html页面
@app.route('/employee_list')
def employee_list():
    return render_template('employee-list.html')


# 访问/employee_detail目录跳转到employee-detail.html页面
@app.route('/employee_detail')
def employee_detail():
    user_id = request.args.get('id')
    return render_template('employee-detail.html', user_id=user_id)


# 访问/employee_add目录跳转到employee-add.html页面
@app.route('/employee_add')
def employee_add():
    return render_template('employee-add.html')


# 访问/employee_edit目录跳转到employee-edit.html页面
@app.route('/employee_edit')
def employee_edit():
    user_id = request.args.get('id')
    return render_template('employee-edit.html', user_id=user_id)


# 访问/employee_charts目录跳转到employee-charts.html页面
@app.route('/employee_charts')
def employee_charts():
    # main1_list = [[30, 20, 36, 10, 8, 5, 30, 20, 36, 10, 8, 18], [30, 20, 36, 10, 8, 18, 10, 8, 5, 30, 20, 36]]
    main2_list = [30, 20, 36, 10, 8, 18]
    main1_list = [employee_c.select_by_resign_date(), employee_c.select_by_hire_date()]
    return render_template('employee-charts.html', main1_list=main1_list, main2_list=main2_list)


# 访问/volunteer_list目录跳转到volunteer-list.html页面
@app.route('/volunteer_list')
def volunteer_list():
    return render_template('volunteer-list.html')


# 访问/volunteer_detail目录跳转到volunteer-detail.html页面
@app.route('/volunteer_detail')
def volunteer_detail():
    user_id = request.args.get('id')
    return render_template('volunteer-detail.html', user_id=user_id)


# 访问/volunteer_add目录跳转到volunteer-add.html页面
@app.route('/volunteer_add')
def volunteer_add():
    return render_template('volunteer-add.html')


# 访问/volunteer_edit目录跳转到volunteer-edit.html页面
@app.route('/volunteer_edit')
def volunteer_edit():
    user_id = request.args.get('id')
    return render_template('volunteer-edit.html', user_id=user_id)


# 访问/volunteer_charts目录跳转到volunteer-charts.html页面
@app.route('/volunteer_charts')
def volunteer_charts():
    main1_list = [[30, 20, 36, 10, 8, 5, 30, 20, 36, 10, 8, 18], [30, 20, 36, 10, 8, 18, 10, 8, 5, 30, 20, 36]]
    main2_list = volunteer_c.select_by_checkin_date()
    return render_template('volunteer-charts.html', main1_list=main1_list, main2_list=main2_list)


# 启动Flask
if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True, port=5000)
