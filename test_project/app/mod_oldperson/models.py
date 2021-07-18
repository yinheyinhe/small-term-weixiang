# -*- coding: utf-8 -*-
# @Time: 2021/7/10 21:02
# @Author: jacksonYuu
# @Software: PyCharm
from app import db


class OldPersoninfo(db.Model):
    __tablename__ = 'oldperson_info'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ORG_ID = db.Column(db.Integer)
    CLIENT_ID = db.Column(db.Integer)
    username = db.Column(db.String(50))
    gender = db.Column(db.String(5))
    phone = db.Column(db.String(50))
    id_card = db.Column(db.String(50))
    birthday = db.Column(db.DateTime)
    checkin_date = db.Column(db.DateTime)
    checkout_date = db.Column(db.DateTime)
    imgset_dir = db.Column(db.String(200))
    profile_photo = db.Column(db.String(200))
    room_number = db.Column(db.String(50))
    firstguardian_name = db.Column(db.String(50))
    firstguardian_relationship = db.Column(db.String(50))
    firstguardian_phone = db.Column(db.String(50))
    firstguardian_wechat = db.Column(db.String(50))
    secondguardian_name = db.Column(db.String(50))
    secondguardian_relationship = db.Column(db.String(50))
    secondguardian_phone = db.Column(db.String(50))
    secondguardian_wechat = db.Column(db.String(50))
    health_state = db.Column(db.String(50))
    description = db.Column(db.String(200))
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
