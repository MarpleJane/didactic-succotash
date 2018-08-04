#coding: utf8
import logging
import datetime

import tornado.escape

from config import BaseController
from config.dmls import *  # TODO


class LoveController(BaseController):
    """/v1/simulation/love_experience"""
    def get(self):
        return


class DregController(BaseController):
    """/v1/simulation/dregs_experience"""
    def get(self):
        return