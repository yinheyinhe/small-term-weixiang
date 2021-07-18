# -*- coding: utf-8 -*-
# @Time: 2021/7/11 11:05
# @Author: jacksonYuu
# @Software: PyCharm
from app import db


class VolunteerInfo(db.Model):
    __tablename__ = 'volunteer_info'

    id = db.Column(db.Integer, primary_key=True)
    ORG_ID = db.Column(db.Integer)
    CLIENT_ID = db.Column(db.Integer)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(5))
    phone = db.Column(db.String(50))
    id_card = db.Column(db.String(50))
    birthday = db.Column(db.DateTime, nullable=True)
    checkin_date = db.Column(db.DateTime, nullable=True)
    checkout_date = db.Column(db.DateTime, nullable=True)
    imgset_dir = db.Column(db.String(200))
    profile_photo = db.Column(db.String(200))
    DESCRIPTION = db.Column(db.String(200))
    isactive = db.Column(db.String(10))
    created = db.Column(db.DateTime)
    CREATEBY = db.Column(db.Integer)
    updated = db.Column(db.DateTime)
    UPDATEBY = db.Column(db.Integer)
    REMOVE = db.Column(db.String(1))

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
