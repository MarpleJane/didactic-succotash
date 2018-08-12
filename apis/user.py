#coding: utf-8
import logging
import datetime

import tornado.escape

from config import BaseController


class UserController(BaseController):
    """/v1/users"""
    def get(self):
        return


class UserLoginController(BaseController):
    """/v1/user_login"""
    def post(self):
        return


class UserInfo(BaseController):
    """/v1/user_info/([0-9]+)"""
    def get(self, user_id):
        return