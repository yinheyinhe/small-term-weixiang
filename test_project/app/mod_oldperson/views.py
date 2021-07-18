# -*- coding: utf-8 -*-
# @Time: 2021/7/10 21:21
# @Author: jacksonYuu
# @Software: PyCharm
import os
import threading
from base64 import b64encode
from os import listdir
from os.path import join

from flask import request, render_template, Blueprint, redirect, url_for, make_response

import app.mod_oldperson.controllers as oldperson_c
from app import app
from app.page_utils import Pagination
from app.util import get_rst, is_image_file

oldperson_view = Blueprint('oldperson_view', __name__)


@oldperson_view.route('/oldperson/findByQuery')
def oldperson_find_by_query():
    page = int(request.args["page"])
    limit = int(request.args["limit"])
    username = request.args.get('username')
    phone = request.args.get('phoneNum')
    gender = request.args.get('status')
    if username == '' and phone == '' and gender == '':
        oldpersons = oldperson_c.get_all_data()
    else:
        oldpersons = oldperson_c.select_by_query(username, phone, gender)
    data = [oldperson.dobule_to_dict() for oldperson in oldpersons]
    rst = get_rst(page, limit, data)
    return rst


@oldperson_view.route('/oldperson/delete', methods=['POST'])
def oldperson_delete():
    ids = request.form.get('ids')
    try:
        oldperson_c.delete_by_ids(ids)
        return {'success': True, 'msg': '删除成功！'}
    except:
        return {'success': False, 'msg': '删除失败！'}


@oldperson_view.route('/oldperson/updateStatus', methods=['POST'])
def oldperson_update_status():
    user_id = request.form.get('id')
    isactive = request.form.get('status')
    try:
        oldperson_c.update_active_by_id(user_id, isactive)
        return {'success': True, 'msg': '修改成功！'}
    except:
        return {'success': False, 'msg': '修改失败！'}


@oldperson_view.route('/oldperson/save', methods=['POST'])
def oldperson_save():
    oldperson_id = request.form.get('id')
    username = request.form.get('username')
    phone = request.form.get('phone')
    id_card = request.form.get('id_card')
    birthday = request.form.get('birthday')
    room_number = request.form.get('room_number')
    firstguardian_name = request.form.get('firstguardian_name')
    firstguardian_relationship = request.form.get('firstguardian_relationship')
    firstguardian_phone = request.form.get('firstguardian_phone')
    secondguardian_name = request.form.get('secondguardian_name')
    secondguardian_relationship = request.form.get('secondguardian_relationship')
    secondguardian_phone = request.form.get('secondguardian_phone')
    health_state = request.form.get('health_state')
    gender = request.form.get('sex')
    if oldperson_id:
        try:
            oldperson_c.update_by_id(oldperson_id, username, phone, id_card, birthday, room_number, firstguardian_name,
                                     firstguardian_relationship, firstguardian_phone, secondguardian_name,
                                     secondguardian_relationship, secondguardian_phone, gender, health_state)
            return {'success': True, 'msg': '修改成功！'}
        except:
            return {'success': False, 'msg': '修改失败！'}
    else:
        try:
            oldperson_c.insert_oldperson(username, phone, id_card, birthday, room_number, firstguardian_name,
                                         firstguardian_relationship, firstguardian_phone, secondguardian_name,
                                         secondguardian_relationship, secondguardian_phone, gender, health_state)
            return {'success': True, 'msg': '新增成功！'}
        except:
            return {'success': False, 'msg': '新增失败！'}


@oldperson_view.route('/oldperson/findById', methods=['POST'])
def oldperson_find_by_id():
    oldperson_id = request.form.get('id')
    try:
        oldperson = oldperson_c.select_by_id(oldperson_id)
        data = oldperson.single_to_dict()
        return data
    except:
        return {}


@oldperson_view.route('/oldperson/imagelist')
def list_all_oldperson_images():
    oldpersons = oldperson_c.get_all_data()
    datalist = [oldperson.dobule_to_dict() for oldperson in oldpersons]
    pager_obj = Pagination(request.args.get("page", 1), len(datalist), request.path, request.args, per_page_count=12)
    index_list = datalist[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("oldperson-images.html", movies=index_list, html=html)


@oldperson_view.route('/oldperson/getImage/<int:oldperson_id>')
def get_oldperson_images(oldperson_id):
    oldperson = oldperson_c.select_by_id(oldperson_id)
    images_dir = app.static_folder + oldperson.imgset_dir + str(oldperson.id)
    _cmd = r'python captureandsavephotos.py  ' + images_dir
    with os.popen(_cmd, "r") as p:
        p.read()
    # start file monitor program, need run in a single thread
    oldperson.imgset_dir = images_dir
    image_filenames = [join(images_dir, x) for x in listdir(images_dir) if is_image_file(x)]
    image_filenames = ['/static' + x.split('static')[1] for x in image_filenames]
    return render_template('oldperson-websocket.html', oldperson_id=oldperson_id, image_filenames=image_filenames)


@oldperson_view.route('/oldperson/setProfileImage/<int:oldperson_id>')
def set_oldperson_profile_image(oldperson_id):
    profile_photo = request.args.get('photo')
    oldperson_c.update_profile_image(oldperson_id, profile_photo)
    return {'success': True, 'msg': '修改成功！'}
