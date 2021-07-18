# -*- coding: utf-8 -*-
# @Time: 2021/7/8 21:46
# @Author: jacksonYuu
# @Software: PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

# 声明Flask
app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")
# 配置数据库信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3000/old_care?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 连接到数据库
db = SQLAlchemy(app)

socketio = SocketIO(app, async_mode='threading')
