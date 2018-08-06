#coding: utf-8
# import logging
# import datetime

# import tornado.escape

# from config import BaseController
# from config.dmls import QUERY_STATEMENTS, USER_LIST


# class ApiQuery(BaseController):
#     "/v1/query"
#     def post(self):
#         delta = datetime.timedelta(days=1)
#         data = tornado.escape.json_decode(self.request.body)
#         user_id = data["user_id"]
#         start_time = data["start_time"] / 1000
#         start_obj = datetime.datetime.fromtimestamp(start_time)
#         end_obj = start_obj + delta

#         dict_result = {}
#         dict_query = {
#             'user_id': user_id,
#             'start_time': start_obj.strftime("%Y-%m-%d"),
#             'end_time': end_obj.strftime("%Y-%m-%d"),
#         }

#         conn = self.get_conn()
#         cursor = self.get_cursor(conn)
#         try:
#             for qs in QUERY_STATEMENTS:
#                 cursor.execute(qs, dict_query)
#                 result = cursor.fetchone()
#                 if result:
#                     dict_result.update(result)
#                 else:
#                     logging.warn(qs)
#         except Exception as e:
#             logging.warn(e)
#             logging.warn(qs)
#             conn.rollback()
#         finally:
#             self.put_conn(conn)

#         if 'grp_use' not in dict_result:
#             dict_result['grp_use'] = 0
        
#         self.write(dict_result)


# class ApiAllUsers(BaseController):
#     "/v1/users"
#     def post(self):
#         result = []
#         data = tornado.escape.json_decode(self.request.body)
#         nick_name = "%" + data["nick_name"] + "%"
#         logging.warn("Nick name: %s", nick_name)
#         ret = 0
#         conn = self.get_conn()
#         cursor = self.get_cursor(conn)
#         try:
#             cursor.execute(USER_LIST, {'nick_name': nick_name})
#             result = cursor.fetchall()
#         except:
#             logging.warn("Fail to get user list")
#             conn.rollback()
#         finally:
#             self.put_conn(conn)
        
#         if not result:
#             ret = 1

#         total = len(result)
        
#         self.write(dict(users=result, ret=ret, total=total))

