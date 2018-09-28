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
        user_data = self.find_data(USERS["FIND_USER"], params)
        ret = 1  # has expection
        if user_data:
            ret = 2  # user exist, then FE should jump to "/v1/get_coins"
            # current_time = self.current_time_obj()
            # need_coins = (current_time - user_data["last_click_login_time"].rsplit(".")[0]).days >= 1
            # self.write(dict(ret=ret, user_data=user_data, need_coins=need_coins))
        else:
            ret = self.insert_data(USERS["USER_INSERT"], params)
            # self.write(dict(ret=ret))
        self.write(dict(ret=ret))


class UserSigninController(BaseController):
    """/v1/user_signin"""
    def post(self):
        w_id = self.get_argument("w_id")
        params = {"w_id": w_id}
        user_data = self.find_data(USERS["FIND_USER"], params)
        ret = 1
        if user_data:
            ret = 0
            current_time = self.current_time_obj()
            need_coins = (current_time - user_data["last_click_login_time"]).days >= 1
            del user_data["create_time"]
            del user_data["last_click_login_time"]
            self.write(dict(ret=ret, user_data=user_data, need_coins=need_coins))
        else:
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
        w_id = self.get_argument("w_id")
        coins = self.get_argument("coins")
        user_id = int(user_id)
        params = {"w_id": w_id}
        user_data = self.find_data(USERS["FIND_USER"], params)
        ret = 1
        if user_data:
            ret = 0
            coin_params = {
                "user_id": user_data["id"],
                "coins": coins
            }
            ret = self.update_data(USERS["COIN_UPDATE"], coin_params)
        self.write(dict(ret=ret))