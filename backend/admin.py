#coding: utf8
import logging
import datetime
import hashlib

import tornado.escape

from config import BaseController
from config.dmls import *  # TODO


class AdminController(BaseController):
    """/v1/admin"""
    def get(self):
        return


class AdminAddController(BaseController):
    """/v1/admin/add"""
    def encrypt(self, pwd):
        h1 = hashlib.md5()
        h1.update(pwd.encode(encoding='utf8'))
        return h1.hexdigest()

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        user_name = data['user_name']
        pwd = data['password']
        real_name = data['real_name']
        status = 1
        pwd = self.encrypt(pwd)
        
        self.write(dict(ret=0))