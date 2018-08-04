#coding: utf8
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

