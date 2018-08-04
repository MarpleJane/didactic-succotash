#coding: utf8
import logging
import datetime

import tornado.escape

from config import BaseController
from config.dmls import *  # TODO


class KiraCampusController(BaseController):
    """/v1/chapter/kira_campus"""
    def get(self):
        return


class KamisamaController(BaseController):
    """/v1/chapter/kamisama"""
    def get(self):
        return