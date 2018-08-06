#coding: utf8
import logging
import datetime

import tornado.escape

from config import BaseController
from config.dmls import CHAPTER


class KiraCampusController(BaseController):
    """/v1/chapter/kira_campus"""
    type_id = 1
    total = {}
    result = {}
    items = []
    page_size = 0

    def get(self):
        self.page_size = self.get_argument("page_size")
        params = {'limit': self.page_size, 'offset': 0, 'type_id': self.type_id}
        ret = 0

        conn = self.get_conn()
        cursor = self.get_cursor(conn)
        try:
            cursor.execute(CHAPTER['CHAPTER_TYPE_SUM'], {'type_id': self.type_id})
            self.total = cursor.fetchone()
            cursor.execute(CHAPTER['CHAPTER_LIMIT'], params)
            self.items = cursor.fetchall()
        except Exception as e:
            logging.warn(e)
            ret = 1
            conn.rollback()
        finally:
            self.put_conn(conn)

        self.result.update(self.total)
        self.result['items'] = self.items
        
        self.write(dict(ret=ret, result=self.result))

    def post(self):
        ret = 0
        data = tornado.escape.json_decode(self.request.body)
        current_page = data['current_page']
        offset = (current_page - 1) * 20
        params = {'limit': self.page_size, 'offset': offset, 'type_id': self.type_id}

        conn = self.get_conn()
        cursor = self.get_cursor(conn)
        try:
            cursor.execute(CHAPTER['CHAPTER_LIMIT'], params)
            self.items = cursor.fetchall()
        except Exception as e:
            ret = 1
            conn.rollback()
        finally:
            self.put_conn(conn)

        self.result['items'] = self.items

        self.write(dict(ret=ret, result=self.result))


class KamisamaController(BaseController):
    """/v1/chapter/kamisama"""
    type_id = 2
    total = {}
    result = {}
    items = []
    page_size = 0

    def get(self):
        self.page_size = self.get_argument("page_size")
        params = {'limit': self.page_size, 'offset': 0, 'type_id': self.type_id}
        ret = 0

        conn = self.get_conn()
        cursor = self.get_cursor(conn)
        try:
            cursor.execute(CHAPTER['CHAPTER_TYPE_SUM'], {'type_id': self.type_id})
            self.total = cursor.fetchone()
            cursor.execute(CHAPTER['CHAPTER_LIMIT'], params)
            self.items = cursor.fetchall()
        except Exception as e:
            logging.warn(e)
            ret = 1
            conn.rollback()
        finally:
            self.put_conn(conn)

        self.result.update(self.total)
        self.result['items'] = self.items
        
        self.write(dict(ret=ret, result=self.result))

    def post(self):
        ret = 0
        data = tornado.escape.json_decode(self.request.body)
        current_page = data['current_page']
        offset = (current_page - 1) * 20
        params = {'limit': self.page_size, 'offset': offset, 'type_id': self.type_id}

        conn = self.get_conn()
        cursor = self.get_cursor(conn)
        try:
            cursor.execute(CHAPTER['CHAPTER_LIMIT'], params)
            self.items = cursor.fetchall()
        except Exception as e:
            ret = 1
            conn.rollback()
        finally:
            self.put_conn(conn)

        self.result['items'] = self.items

        self.write(dict(ret=ret, result=self.result))


class ChapterAddNewController(BaseController):
    """/v1/add_new/chapter"""
    ADD_NEW = 0
    EDIT = 1

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        edit = data['edit']
        form = data['form']
        ret = 0
        # now = datetime.datetime.now()
        # update_time = now.strftime("%Y-%m-%d %H:%M:%S")
        form['update_time'] = self.current_time()

        if edit == self.ADD_NEW:
            ret = self.insert_data(CHAPTER['INSERT_CHAPTER'], form)
        elif edit == self.EDIT:
            form['plot_id'] = form['id']
            total = self.select_all(CHAPTER['FIND_CHAPTER'], {'plot_id': form['id']})
            if total:
                ret = self.update_data(CHAPTER['UPDATE_CHAPTER'], form)
            else:
                logging.warn("the plot, id=%d is not exist", form['id'])
                ret = 1

        self.write(dict(ret=ret))


class ChapterDelController(BaseController):
    """/v1/del/chapter"""
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        params = {'plot_id': data['plot_id'], 'update_time': self.current_time()}
        # plot_id = data['plot_id']
        # update_time = self.current_time()
        # ret = self.delete_data(CHAPTER['DELETE_CHAPTER'], {'plot_id': plot_id, 'update_time': update_time})
        ret = self.delete_data(CHAPTER['DELETE_CHAPTER'], params)
        self.write(dict(ret=ret))