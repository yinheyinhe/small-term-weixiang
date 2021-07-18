# -*- coding: utf-8 -*-
# @Time: 2021/7/10 21:31
# @Author: jacksonYuu
# @Software: PyCharm
import json
import os
import time

from flask import make_response, request


def get_rst(page, limit, data):
    aaa = {"code": 0, "msg": "", "data": data}
    aaa["count"] = len(aaa["data"])
    aaa["data"] = aaa["data"][(page - 1) * 10: (page - 1) * 10 + limit]
    rst = make_response(json.dumps(aaa))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])
