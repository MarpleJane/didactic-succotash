#coding: utf8
import logging
import datetime
import hashlib

import tornado.escape

from config import BaseController


class UploadPictureController(BaseController):
    """/upload/picture"""
    def post(self):
        file_meta = self.request.files['obj'][0]
        file_extension = file_meta['filename'].split(".")[-1]
        file_stream = file_meta['body']
        md5 = hashlib.md5(file_stream).hexdigest()

        today_date = self.today_date()
        key = "simulation" + "/" + today_date + "/" + md5 + "." + file_extension
        token = self.generate_token(key)

        url = self.upload_file(token, key, file_stream)
        logging.warn(url)

        self.write(dict(url=url))