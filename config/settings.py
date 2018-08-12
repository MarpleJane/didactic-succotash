#coding: utf-8
import psycopg2
import psycopg2.extras
from psycopg2.pool import SimpleConnectionPool


# Database setting
# PG_DB = {
#     "db": "postgres",
#     "user": "otaku",
#     "pwd": "123456",
#     "host": "106.75.210.68",
#     "port": "12345",
#     "minconn": 5,  # 最小连接数
#     "maxconn": 200  # 最大连接数
# }

# PG_DB = {
#     "db": "postgres",
#     "user": "otaku",
#     "pwd": "m0em0e@db",
#     "host": "10.10.33.159",
#     "port": "12345",
#     "minconn": 5,  # 最小连接数
#     "maxconn": 200  # 最大连接数
# }

PG_DB = {
    "db": "wechat_gal",
    "user": "postgres",
    "pwd": "root",
    "host": "127.0.0.1",
    "port": "5432",
    "minconn": 5,  # 最小连接数
    "maxconn": 200  # 最大连接数
}

POOL = SimpleConnectionPool(
    PG_DB["minconn"], 
    PG_DB["maxconn"],
    database=PG_DB["db"],
    user=PG_DB["user"],
    password=PG_DB["pwd"],
    host=PG_DB["host"],
    port=PG_DB["port"],
)

QINIU = {
    "ACCESS_KEY": "epbKZnxFUtJ9bTWufWtvXkAwtsseutpa8xRpJ3KI",
    "SECURE_KEY": "TEWIuwOCs9KTeRqrOuQEDmUHDDd6RYBkoZ32m2Is",
    # "BUCKET": "otaku-test-1",
    "BUCKET": "otaku-resource",
    "PREFIX": "http://source.moemoe.la/"
}