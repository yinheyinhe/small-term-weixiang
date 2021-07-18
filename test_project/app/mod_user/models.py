# -*- coding: utf-8 -*-
# @Time: 2021/7/9 9:21
# @Author: jacksonYuu
# @Software: PyCharm
from app import db


class User(db.Model):
    __tablename__ = 'sys_user'
    # columss
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=True)
    sex = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(80), nullable=True)
    phone = db.Column(db.String(80), nullable=True)
    isactive = db.Column(db.String(10), default='1', nullable=True)
    created = db.Column(db.DateTime, nullable=True)
    updated = db.Column(db.DateTime, nullable=True)

    # 多个对象
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    # 单个对象方法
    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
