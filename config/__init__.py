#coding: utf8
import logging
import datetime

import psycopg2.extras
import psycopg2.extensions
from tornado.web import RequestHandler

from .settings import POOL


DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: float(value) if value is not None else None)
psycopg2.extensions.register_type(DEC2FLOAT)


class BaseController(RequestHandler):
    __pool = POOL

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get_conn(self):
        return self.__pool.getconn()

    def get_cursor(self, conn):
        return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def put_conn(self, conn):
        self.__pool.putconn(conn)

    def select_all(self, statement, params):
        conn = self.get_conn()
        cursor = self.get_cursor(conn)
        total = 0
        try:
            cursor.execute(statement, params)
            total = cursor.fetchall()
        except Exception as e:
            logging.warn(e)
            conn.rollback()
        finally:
            self.put_conn(conn)
        return total

    def insert_data(self, statement, params):
        conn = self.get_conn()
        cursor = self.get_cursor(conn)
        ret = 0
        try:
            cursor.execute(statement, params)
            conn.commit()
        except Exception as e:
            ret = 1
            logging.warn(e)
            conn.rollback()
        finally:
            self.put_conn(conn)
        return ret

    def update_data(self, statement, params):
        return self.insert_data(statement, params)
        # conn = self.get_conn()
        # cursor = self.get_cursor(conn)
        # ret = 0
        # try:
        #     cursor.execute(statement, params)
        #     conn.commit()
        # except Exception as e:
        #     logging.warn(e)
        #     conn.rollback()
        #     ret = 1
        # finally:
        #     self.put_conn(conn)
        # return ret

    def delete_data(self, statement, params):
        return self.insert_data(statement, params)

    def current_time(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return current_time


