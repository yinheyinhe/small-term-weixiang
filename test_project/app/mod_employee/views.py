# -*- coding: utf-8 -*-
# @Time: 2021/7/11 11:14
# @Author: jacksonYuu
# @Software: PyCharm
import os
from os import listdir
from os.path import join

from flask import request, render_template, Blueprint, redirect, url_for, make_response

import app.mod_employee.controllers as employee_c
from app import app
from app.page_utils import Pagination
from app.util import get_rst, is_image_file

employee_view = Blueprint('employee_view', __name__)


@employee_view.route('/employee/findByQuery')
def employee_find_by_query():
    page = int(request.args["page"])
    limit = int(request.args["limit"])
    username = request.args.get('username')
    phone = request.args.get('phoneNum')
    gender = request.args.get('status')
    if username == '' and phone == '' and gender == '':
        employees = employee_c.get_all_data()
    else:
        employees = employee_c.select_by_query(username, phone, gender)
    data = [employee.dobule_to_dict() for employee in employees]
    rst = get_rst(page, limit, data)
    return rst


@employee_view.route('/employee/delete', methods=['POST'])
def employee_delete():
    ids = request.form.get('ids')
    try:
        employee_c.delete_by_ids(ids)
        return {'success': True, 'msg': '删除成功！'}
    except:
        return {'success': False, 'msg': '删除失败！'}


@employee_view.route('/employee/updateStatus', methods=['POST'])
def employee_update_status():
    user_id = request.form.get('id')
    isactive = request.form.get('status')
    try:
        employee_c.update_active_by_id(user_id, isactive)
        return {'success': True, 'msg': '修改成功！'}
    except:
        return {'success': False, 'msg': '修改失败！'}


@employee_view.route('/employee/save', methods=['POST'])
def employee_save():
    employee_id = request.form.get('id')
    username = request.form.get('username')
    phone = request.form.get('phone')
    id_card = request.form.get('id_card')
    birthday = request.form.get('birthday')
    gender = request.form.get('sex')
    if employee_id:
        try:
            employee_c.update_by_id(employee_id, username, phone, id_card, birthday, gender)
            return {'success': True, 'msg': '修改成功！'}
        except:
            return {'success': False, 'msg': '修改失败！'}
    else:
        try:
            employee_c.insert_employee(username, phone, id_card, birthday, gender)
            return {'success': True, 'msg': '新增成功！'}
        except:
            return {'success': False, 'msg': '新增失败！'}


@employee_view.route('/employee/findById', methods=['POST'])
def employee_find_by_id():
    employee_id = request.form.get('id')
    try:
        employee = employee_c.select_by_id(employee_id)
        data = employee.single_to_dict()
        return data
    except:
        return {}


@employee_view.route('/employee/imagelist')
def list_all_employee_images():
    employees = employee_c.get_all_data()
    datalist = [employee.dobule_to_dict() for employee in employees]
    pager_obj = Pagination(request.args.get("page", 1), len(datalist), request.path, request.args, per_page_count=12)
    index_list = datalist[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("employee-images.html", movies=index_list, html=html)


@employee_view.route('/employee/getImage/<int:employee_id>')
def get_employee_images(employee_id):
    employee = employee_c.select_by_id(employee_id)
    images_dir = app.static_folder + employee.imgset_dir + str(employee.id)
    _cmd = r'python captureandsavephotos.py  ' + images_dir
    with os.popen(_cmd, "r") as p:
        p.read()
    # start file monitor program, need run in a single thread
    employee.imgset_dir = images_dir
    image_filenames = [join(images_dir, x) for x in listdir(images_dir) if is_image_file(x)]
    image_filenames = ['/static' + x.split('static')[1] for x in image_filenames]
    return render_template('employee-websocket.html', employee_id=employee_id, image_filenames=image_filenames)


@employee_view.route('/employee/setProfileImage/<int:employee_id>')
def set_employee_profile_image(employee_id):
    profile_photo = request.args.get('photo')
    employee_c.update_profile_image(employee_id, profile_photo)
    return {'success': True, 'msg': '修改成功！'}
