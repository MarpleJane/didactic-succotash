#coding: utf-8
import logging
import datetime

import tornado.escape

from config import BaseController
from config.dmls_api import USERS


class UserRankController(BaseController):
    """/v1/user_rank"""
    def get(self):
        limit = self.get_argument("limit")
        rank_list = self.select_all(USERS["USER_RANK"], {"limit": limit})
        self.write(dict(rank_list=rank_list))


class UserSignupController(BaseController):
    """/v1/user_signup"""
    def post(self):
        user_name = self.get_argument("user_name")
        avatar = self.get_argument("avatar")
        w_id = self.get_argument("w_id")
        params = {"user_name": user_name, "avatar": avatar, "w_id": w_id}
        ret = self.insert_data(USERS["USER_INSERT"], params)
        self.write(dict(ret=ret))


class UserInfo(BaseController):
    """/v1/user_info/([0-9]+)"""
    def get(self, user_id):
        user_id = int(user_id)
        params = {"challenger_id": user_id}
        user_info = self.select_all(USERS["USER_INFO"], params)
        user_info = user_info[0]
        self.write(dict(user_info=user_info))


class GetCoinsController(BaseController):
    """/v1/get_coins/([0-9]+)"""
    def post(self, user_id):
        coins = self.get_argument("coins")
        user_id = int(user_id)
        params = {"user_id", "coins"}
        ret = self.update_data(USERS["COIN_UPDATE"], params)
        self.write(dict(ret=ret))