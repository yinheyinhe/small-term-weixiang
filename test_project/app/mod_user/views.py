# -*- coding: utf-8 -*-
# @Time: 2021/7/10 21:27
# @Author: jacksonYuu
# @Software: PyCharm
from flask import request, render_template, Blueprint, redirect, url_for, make_response, flash

import app.mod_user.controllers as user_c
from app.util import get_rst

user_view = Blueprint('user_view', __name__)


@user_view.route('/user/findByQuery')
def user_find_by_query():
    page = int(request.args["page"])
    limit = int(request.args["limit"])
    username = request.args.get('username')
    phone = request.args.get('phoneNum')
    sex = request.args.get('status')
    if username == '' and phone == '' and sex == '':
        users = user_c.get_all_user()
    else:
        users = user_c.select_by_query(username, phone, sex)
    data = [user.dobule_to_dict() for user in users]
    rst = get_rst(page, limit, data)
    return rst


@user_view.route('/user/delete', methods=['POST'])
def user_delete():
    ids = request.form.get('ids')
    try:
        user_c.delete_by_ids(ids)
        return {'success': True, 'msg': '删除成功！'}
    except:
        return {'success': False, 'msg': '删除失败！'}


@user_view.route('/user/updateStatus', methods=['POST'])
def user_update_status():
    user_id = request.form.get('id')
    isactive = request.form.get('status')
    try:
        user_c.update_active_by_id(user_id, isactive)
        return {'success': True, 'msg': '修改成功！'}
    except:
        return {'success': False, 'msg': '修改失败！'}


@user_view.route('/user/save', methods=['POST'])
def user_save():
    user_id = request.form.get('id')
    username = request.form.get('username')
    password = request.form.get('password')
    phone = request.form.get('phone')
    email = request.form.get('email')
    sex = request.form.get('sex')
    if user_id:
        try:
            user_c.update_by_id(user_id, username, password, phone, email, sex)
            return {'success': True, 'msg': '修改成功！'}
        except:
            return {'success': False, 'msg': '修改失败！'}
    else:
        try:
            user_c.insert_user(username, password, phone, email, sex)
            return {'success': True, 'msg': '新增成功！'}
        except:
            return {'success': False, 'msg': '新增失败！'}


@user_view.route('/user/findById', methods=['POST'])
def user_find_by_id():
    user_id = request.form.get('id')
    try:
        user = user_c.select_by_id(user_id)
        data = user.single_to_dict()
        return data
    except:
        return {}
