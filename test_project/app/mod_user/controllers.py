# -*- coding: utf-8 -*-
# @Time: 2021/7/9 9:25
# @Author: jacksonYuu
# @Software: PyCharm
import time

from app import db
from app.mod_user.models import User


def get_all_user():
    return User.query.all()


def select_by_query(username, phone, sex):
    filter_map = []
    if username:
        filter_map.append(User.username.like(username))
    if phone:
        filter_map.append(User.phone.like(phone))
    if sex:
        filter_map.append(User.sex.in_(sex.split(',')))
    return User.query.filter(*filter_map)


def select_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def select_by_username(username):
    return User.query.filter_by(username=username).first()


def register_user(username, password, phone, sex):
    created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = User(username=username, password=password, phone=phone, email=None, sex=sex, created=created, updated=None)
    db.session.add(user)
    db.session.commit()


def insert_user(username, password, phone, email, sex):
    created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = User(username=username, password=password, phone=phone, email=email, sex=sex, created=created, updated=None)
    db.session.add(user)
    db.session.commit()


def change_pass_username(username, new_pass):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dbUser = User.query.filter_by(username=username).first()  # 先根据 id 查出数据库的一条数据
    dbUser.password = new_pass  # 修改密码
    dbUser.updated = updated  # 修改时间
    db.session.commit()  # 提交数据库


def select_by_password(name, password):
    return User.query.filter_by(username=name, password=password).first()


def delete_by_ids(ids):
    users = User.query.filter(User.id.in_(ids.split(','))).all()
    [db.session.delete(u) for u in users]
    db.session.commit()


def update_active_by_id(user_id, isactive):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    users = User.query.filter_by(id=user_id).first()
    users.isactive = isactive
    users.updated = updated
    db.session.commit()


def update_by_id(user_id, username, password, phone, email, sex):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dbUser = User.query.filter_by(id=user_id).first()  # 先根据 id 查出数据库的一条数据
    dbUser.username = username
    dbUser.password = password  # 修改密码
    dbUser.phone = phone
    dbUser.email = email
    dbUser.sex = sex
    dbUser.updated = updated  # 修改时间
    db.session.commit()  # 提交数据库
