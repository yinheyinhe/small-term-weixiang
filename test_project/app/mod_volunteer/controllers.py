# -*- coding: utf-8 -*-
# @Time: 2021/7/11 11:07
# @Author: jacksonYuu
# @Software: PyCharm
import time

from sqlalchemy import extract

from app.mod_volunteer.models import VolunteerInfo
from app import db


def get_all_data():
    return VolunteerInfo.query.all()


def select_by_id(volunteer_id):
    return VolunteerInfo.query.filter_by(id=volunteer_id).first()


def select_by_query(name, phone, gender):
    filter_map = []
    if name:
        filter_map.append(VolunteerInfo.name.like(name))
    if phone:
        filter_map.append(VolunteerInfo.phone.like(phone))
    if gender:
        filter_map.append(VolunteerInfo.gender.in_(gender.split(',')))
    return VolunteerInfo.query.filter(*filter_map)


def delete_by_ids(ids):
    volunteers = VolunteerInfo.query.filter(VolunteerInfo.id.in_(ids.split(','))).all()
    [db.session.delete(u) for u in volunteers]
    db.session.commit()


def update_active_by_id(volunteer_id, isactive):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    volunteer = VolunteerInfo.query.filter_by(id=volunteer_id).first()
    volunteer.isactive = isactive
    volunteer.updated = updated
    if volunteer.checkout_date:
        volunteer.checkout_date = None
    else:
        volunteer.checkout_date = updated
    db.session.commit()


def update_by_id(volunteer_id, name, phone, id_card, birthday, gender):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    volunteer = VolunteerInfo.query.filter_by(id=volunteer_id).first()  # 先根据 id 查出数据库的一条数据
    volunteer.name = name
    volunteer.phone = phone
    volunteer.id_card = id_card
    volunteer.birthday = birthday
    volunteer.gender = gender
    volunteer.updated = updated  # 修改时间
    db.session.commit()  # 提交数据库


def delete_by_id(volunteer_id):
    record = VolunteerInfo.query.filter_by(id=volunteer_id).first()
    db.session.delete(record)
    db.session.commit()


def insert_volunteer(name, phone, id_card, birthday, gender):
    created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    volunteer = VolunteerInfo()
    volunteer.name = name
    volunteer.phone = phone
    volunteer.id_card = id_card
    volunteer.birthday = birthday
    volunteer.gender = gender
    volunteer.created = created
    volunteer.checkin_date = created
    db.session.add(volunteer)
    db.session.commit()


def select_by_checkin_date():
    c_all = []
    # 查询每个月访问人数
    for i in range(1, 13):
        c_all.append(VolunteerInfo.query.filter(extract('month', VolunteerInfo.checkin_date) == i).count())
    return c_all


def update_profile_image(volunteer_id, profile_photo):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    volunteer = VolunteerInfo.query.filter_by(id=volunteer_id).first()
    volunteer.updated = updated
    volunteer.profile_photo = profile_photo
    db.session.commit()
