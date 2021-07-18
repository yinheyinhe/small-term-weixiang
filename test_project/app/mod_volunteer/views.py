# -*- coding: utf-8 -*-
# @Time: 2021/7/11 11:14
# @Author: jacksonYuu
# @Software: PyCharm
import os
from os import listdir
from os.path import join

from flask import request, render_template, Blueprint, redirect, url_for, make_response

import app.mod_volunteer.controllers as volunteer_c
from app import app
from app.page_utils import Pagination
from app.util import get_rst

volunteer_view = Blueprint('volunteer_view', __name__)


@volunteer_view.route('/volunteer/findByQuery')
def volunteer_find_by_query():
    page = int(request.args["page"])
    limit = int(request.args["limit"])
    name = request.args.get('username')
    phone = request.args.get('phoneNum')
    gender = request.args.get('status')
    if name == '' and phone == '' and gender == '':
        volunteers = volunteer_c.get_all_data()
    else:
        volunteers = volunteer_c.select_by_query(name, phone, gender)
    data = [volunteer.dobule_to_dict() for volunteer in volunteers]
    rst = get_rst(page, limit, data)
    return rst


@volunteer_view.route('/volunteer/delete', methods=['POST'])
def volunteer_delete():
    ids = request.form.get('ids')
    try:
        volunteer_c.delete_by_ids(ids)
        return {'success': True, 'msg': '删除成功！'}
    except:
        return {'success': False, 'msg': '删除失败！'}


@volunteer_view.route('/volunteer/updateStatus', methods=['POST'])
def volunteer_update_status():
    user_id = request.form.get('id')
    isactive = request.form.get('status')
    try:
        volunteer_c.update_active_by_id(user_id, isactive)
        return {'success': True, 'msg': '修改成功！'}
    except:
        return {'success': False, 'msg': '修改失败！'}


@volunteer_view.route('/volunteer/save', methods=['POST'])
def volunteer_save():
    volunteer_id = request.form.get('id')
    name = request.form.get('username')
    phone = request.form.get('phone')
    id_card = request.form.get('id_card')
    birthday = request.form.get('birthday')
    gender = request.form.get('sex')
    if volunteer_id:
        try:
            volunteer_c.update_by_id(volunteer_id, name, phone, id_card, birthday, gender)
            return {'success': True, 'msg': '修改成功！'}
        except:
            return {'success': False, 'msg': '修改失败！'}
    else:
        try:
            volunteer_c.insert_volunteer(name, phone, id_card, birthday, gender)
            return {'success': True, 'msg': '新增成功！'}
        except:
            return {'success': False, 'msg': '新增失败！'}


@volunteer_view.route('/volunteer/findById', methods=['POST'])
def volunteer_find_by_id():
    volunteer_id = request.form.get('id')
    try:
        volunteer = volunteer_c.select_by_id(volunteer_id)
        data = volunteer.single_to_dict()
        return data
    except:
        return {}


@volunteer_view.route('/volunteer/imagelist')
def list_all_volunteer_images():
    volunteers = volunteer_c.get_all_data()
    datalist = [volunteer.dobule_to_dict() for volunteer in volunteers]
    pager_obj = Pagination(request.args.get("page", 1), len(datalist), request.path, request.args, per_page_count=12)
    index_list = datalist[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("volunteer-images.html", movies=index_list, html=html)


@volunteer_view.route('/volunteer/getImage/<int:volunteer_id>')
def get_volunteer_images(volunteer_id):
    volunteer = volunteer_c.select_by_id(volunteer_id)
    images_dir = app.static_folder + volunteer.imgset_dir + str(volunteer.id)
    _cmd = r'python captureandsavephotos.py  ' + images_dir
    with os.popen(_cmd, "r") as p:
        p.read()
    # start file monitor program, need run in a single thread
    volunteer.imgset_dir = images_dir
    image_filenames = [join(images_dir, x) for x in listdir(images_dir) if is_image_file(x)]
    image_filenames = ['/static' + x.split('static')[1] for x in image_filenames]
    return render_template('volunteer-websocket.html', volunteer_id=volunteer_id, image_filenames=image_filenames)


@volunteer_view.route('/volunteer/setProfileImage/<int:volunteer_id>')
def set_volunteer_profile_image(volunteer_id):
    profile_photo = request.args.get('photo')
    volunteer_c.update_profile_image(volunteer_id, profile_photo)
    return {'success': True, 'msg': '修改成功！'}
