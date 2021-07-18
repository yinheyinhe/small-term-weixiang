# -*- coding: utf-8 -*-
# @Time: 2021/7/10 21:06
# @Author: jacksonYuu
# @Software: PyCharm
import datetime
import time

from sqlalchemy import extract

from app.mod_oldperson.models import OldPersoninfo
from app import db


def get_all_data():
    return OldPersoninfo.query.all()


def select_by_id(oldperson_id):
    return OldPersoninfo.query.filter_by(id=oldperson_id).first()


def select_by_username(oldperson_username):
    return OldPersoninfo.query.filter_by(username=oldperson_username).first()


def select_by_query(username, phone, gender):
    filter_map = []
    if username:
        filter_map.append(OldPersoninfo.username.like(username))
    if phone:
        filter_map.append(OldPersoninfo.phone.like(phone))
    if gender:
        filter_map.append(OldPersoninfo.gender.in_(gender.split(',')))
    return OldPersoninfo.query.filter(*filter_map)


def delete_by_ids(ids):
    oldpersons = OldPersoninfo.query.filter(OldPersoninfo.id.in_(ids.split(','))).all()
    [db.session.delete(u) for u in oldpersons]
    db.session.commit()


def update_active_by_id(oldperson_id, isactive):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    oldperson = OldPersoninfo.query.filter_by(id=oldperson_id).first()
    oldperson.isactive = isactive
    oldperson.updated = updated
    if oldperson.checkout_date:
        oldperson.checkout_date = None
    else:
        oldperson.checkout_date = updated
    db.session.commit()

def update_profile_image(oldperson_id, profile_photo):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    oldperson = OldPersoninfo.query.filter_by(id=oldperson_id).first()
    oldperson.updated = updated
    oldperson.profile_photo = profile_photo
    db.session.commit()


def select_oldperson_by_age():
    # 查询60岁以下人数
    c_1 = OldPersoninfo.query.filter(extract('year', OldPersoninfo.birthday) + 60 > datetime.date.today().year).count()
    # 查询60-65岁人数
    c_2 = OldPersoninfo.query.filter(extract('year', OldPersoninfo.birthday) + 65 > datetime.date.today().year).filter(
        extract('year', OldPersoninfo.birthday) + 60 <= datetime.date.today().year).count()
    # 查询65-70岁人数
    c_3 = OldPersoninfo.query.filter(extract('year', OldPersoninfo.birthday) + 70 > datetime.date.today().year).filter(
        extract('year', OldPersoninfo.birthday) + 65 <= datetime.date.today().year).count()
    # 查询70-75岁人数
    c_4 = OldPersoninfo.query.filter(extract('year', OldPersoninfo.birthday) + 75 > datetime.date.today().year).filter(
        extract('year', OldPersoninfo.birthday) + 70 <= datetime.date.today().year).count()
    # 查询70-75岁人数
    c_5 = OldPersoninfo.query.filter(extract('year', OldPersoninfo.birthday) + 80 > datetime.date.today().year).filter(
        extract('year', OldPersoninfo.birthday) + 75 <= datetime.date.today().year).count()
    # 查询80岁以上人数
    c_6 = OldPersoninfo.query.filter(extract('year', OldPersoninfo.birthday) + 80 <= datetime.date.today().year).count()
    return [c_1, c_2, c_3, c_4, c_5, c_6]


def update_by_id(oldperson_id, username, phone, id_card, birthday, room_number, firstguardian_name,
                 firstguardian_relationship, firstguardian_phone, secondguardian_name,
                 secondguardian_relationship, secondguardian_phone, gender, health_state):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dbOldperson = OldPersoninfo.query.filter_by(id=oldperson_id).first()  # 先根据 id 查出数据库的一条数据
    dbOldperson.username = username
    dbOldperson.phone = phone
    dbOldperson.id_card = id_card
    dbOldperson.birthday = birthday
    dbOldperson.room_number = room_number
    dbOldperson.firstguardian_name = firstguardian_name
    dbOldperson.firstguardian_relationship = firstguardian_relationship
    dbOldperson.firstguardian_phone = firstguardian_phone
    dbOldperson.secondguardian_name = secondguardian_name
    dbOldperson.secondguardian_relationship = secondguardian_relationship
    dbOldperson.secondguardian_phone = secondguardian_phone
    dbOldperson.gender = gender
    dbOldperson.health_state = health_state
    dbOldperson.updated = updated  # 修改时间
    db.session.commit()  # 提交数据库


def delete_by_id(oldperson_id):
    record = OldPersoninfo.query.filter_by(id=oldperson_id).first()
    db.session.delete(record)
    db.session.commit()


def insert_oldperson(username, phone, id_card, birthday, room_number, firstguardian_name,
                     firstguardian_relationship, firstguardian_phone, secondguardian_name,
                     secondguardian_relationship, secondguardian_phone, gender, health_state):
    created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    oldperson = OldPersoninfo()
    oldperson.username = username
    oldperson.phone = phone
    oldperson.id_card = id_card
    oldperson.birthday = birthday
    oldperson.room_number = room_number
    oldperson.firstguardian_name = firstguardian_name
    oldperson.firstguardian_relationship = firstguardian_relationship
    oldperson.firstguardian_phone = firstguardian_phone
    oldperson.secondguardian_name = secondguardian_name
    oldperson.secondguardian_relationship = secondguardian_relationship
    oldperson.secondguardian_phone = secondguardian_phone
    oldperson.gender = gender
    oldperson.health_state = health_state
    oldperson.created = created
    oldperson.checkin_date = created
    db.session.add(oldperson)
    db.session.commit()
