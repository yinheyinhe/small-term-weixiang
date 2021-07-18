# -*- coding: utf-8 -*-
# @Time: 2021/7/11 11:07
# @Author: jacksonYuu
# @Software: PyCharm
import datetime
import time

from sqlalchemy import extract

from app.mod_employee.models import EmployeeInfo
from app import db


def get_all_data():
    return EmployeeInfo.query.all()


def select_by_id(employee_id):
    return EmployeeInfo.query.filter_by(id=employee_id).first()


def select_by_query(username, phone, gender):
    filter_map = []
    if username:
        filter_map.append(EmployeeInfo.username.like(username))
    if phone:
        filter_map.append(EmployeeInfo.phone.like(phone))
    if gender:
        filter_map.append(EmployeeInfo.gender.in_(gender.split(',')))
    return EmployeeInfo.query.filter(*filter_map)


def delete_by_ids(ids):
    employees = EmployeeInfo.query.filter(EmployeeInfo.id.in_(ids.split(','))).all()
    [db.session.delete(u) for u in employees]
    db.session.commit()


def update_active_by_id(employee_id, isactive):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    employee = EmployeeInfo.query.filter_by(id=employee_id).first()
    employee.isactive = isactive
    employee.updated = updated
    if employee.resign_date:
        employee.resign_date = None
    else:
        employee.resign_date = updated
    db.session.commit()


def update_by_id(employee_id, username, phone, id_card, birthday, gender):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    employee = EmployeeInfo.query.filter_by(id=employee_id).first()  # 先根据 id 查出数据库的一条数据
    employee.username = username
    employee.phone = phone
    employee.id_card = id_card
    employee.birthday = birthday
    employee.gender = gender
    employee.updated = updated  # 修改时间
    db.session.commit()  # 提交数据库


def delete_by_id(employee_id):
    record = EmployeeInfo.query.filter_by(id=employee_id).first()
    db.session.delete(record)
    db.session.commit()


def insert_employee(username, phone, id_card, birthday, gender):
    created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    employee = EmployeeInfo()
    employee.username = username
    employee.phone = phone
    employee.id_card = id_card
    employee.birthday = birthday
    employee.gender = gender
    employee.created = created
    employee.hire_date = created
    db.session.add(employee)
    db.session.commit()


def select_by_hire_date():
    c_all = []
    # 查询每个月入职人数
    for i in range(1, 13):
        c_all.append(EmployeeInfo.query.filter(extract('month', EmployeeInfo.hire_date) == i).count())
    return c_all


def select_by_resign_date():
    c_all = []
    # 查询每个月离职人数
    for i in range(1, 13):
        c_all.append(EmployeeInfo.query.filter(extract('month', EmployeeInfo.resign_date) == i).count())
    return c_all


def update_profile_image(employee_id, profile_photo):
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    employee = EmployeeInfo.query.filter_by(id=employee_id).first()
    employee.updated = updated
    employee.profile_photo = profile_photo
    db.session.commit()
