#coding: utf-8


USER_NAME = """
    SELECT nick_name FROM t_user_info
      WHERE user_id = %(user_id)s
"""

NUM_DOC = """
    SELECT COALESCE(COUNT(*), 0) AS num_doc, COALESCE(SUM(comments), 0) AS num_doc_com, COALESCE(SUM(likes), 0) AS num_doc_liked, COALESCE(SUM(read_num), 0) AS num_doc_readed
      FROM t_doc_detail
        WHERE create_user = %(user_id)s
          AND create_time >= %(start_time)s
          AND create_time < %(end_time)s
""" 

NUM_REPLY = """
    SELECT COALESCE(COUNT(*), 0) AS num_reply FROM t_user_reply
      WHERE from_user = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
"""

NUM_TAG = """
    SELECT COALESCE(SUM(num), 0) AS num_tag FROM (
        SELECT COUNT(*) AS num FROM t_tag_1 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_2 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_3 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_4 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_5 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_6 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_7 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_8 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_9 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_10 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
    ) AS doc_tag
"""

NUM_TAG_LIKE = """
    SELECT COALESCE(SUM(num), 0) AS num_tag_like FROM (
        SELECT COUNT(*) AS num FROM t_tag_like_1 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_2 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_3 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_4 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_5 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_6 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_7 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_8 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_9 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_tag_like_10 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
    ) AS user_tag_like
"""

NUM_DOC_LIKE = """
    SELECT COALESCE(SUM(num), 0) AS num_doc_like FROM (
        SELECT COUNT(*) AS num FROM t_like_1 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_2 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_3 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_4 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_5 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_6 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_7 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_8 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_9 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_like_10 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
    ) AS user_doc_like
"""

NUM_TAG_LIKED = """
    SELECT COALESCE(SUM(num), 0) AS num_tag_liked FROM (
        SELECT SUM(user_tag_like_1.like) AS num FROM (
            SELECT * FROM t_tag_1 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_1
        LEFT JOIN t_tag_like_1 user_tag_like_1 ON user_tag_1.id = user_tag_like_1.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_2.like) AS num FROM (
            SELECT * FROM t_tag_2 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_2
        LEFT JOIN t_tag_like_2 user_tag_like_2 ON user_tag_2.id = user_tag_like_2.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_3.like) AS num FROM (
            SELECT * FROM t_tag_3 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_3
        LEFT JOIN t_tag_like_3 user_tag_like_3 ON user_tag_3.id = user_tag_like_3.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_4.like) AS num FROM (
            SELECT * FROM t_tag_4 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_4
        LEFT JOIN t_tag_like_4 user_tag_like_4 ON user_tag_4.id = user_tag_like_4.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_5.like) AS num FROM (
            SELECT * FROM t_tag_5 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_5
        LEFT JOIN t_tag_like_5 user_tag_like_5 ON user_tag_5.id = user_tag_like_5.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_6.like) AS num FROM (
            SELECT * FROM t_tag_6 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_6
        LEFT JOIN t_tag_like_6 user_tag_like_6 ON user_tag_6.id = user_tag_like_6.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_7.like) AS num FROM (
            SELECT * FROM t_tag_7 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_7
        LEFT JOIN t_tag_like_7 user_tag_like_7 ON user_tag_7.id = user_tag_like_7.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_8.like) AS num FROM (
            SELECT * FROM t_tag_8 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_8
        LEFT JOIN t_tag_like_8 user_tag_like_8 ON user_tag_8.id = user_tag_like_8.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_9.like) AS num FROM (
            SELECT * FROM t_tag_9 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_9
        LEFT JOIN t_tag_like_9 user_tag_like_9 ON user_tag_9.id = user_tag_like_9.tag_id
        UNION ALL
        SELECT SUM(user_tag_like_10.like) AS num FROM (
            SELECT * FROM t_tag_10 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        ) AS user_tag_10
        LEFT JOIN t_tag_like_10 user_tag_like_10 ON user_tag_10.id = user_tag_like_10.tag_id
    ) AS user_liked
"""

NUM_READ = """
    SELECT COALESCE(COUNT(*), 0) AS num_read FROM log_doc_comment_click
      WHERE user_id = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
        AND name LIKE '社团%%'
"""

NUM_STAY = """
    SELECT COALESCE(SUM(stay_time), 0) AS num_stay FROM log_department_stay
      WHERE user_id = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
        AND name LIKE '社团%%'
"""

NUM_PRIVATE = """
    SELECT COALESCE(COUNT(*), 0) AS num_private FROM t_talk_message
      WHERE create_user = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
"""

NUM_DEL = """
    SELECT COALESCE(COUNT(*), 0) AS num_del FROM t_doc_detail
      WHERE create_user = %(user_id)s
"""

NUM_FRO = """
    SELECT COALESCE(COUNT(*), 0) AS num_fro FROM t_user_frozen_record
      WHERE user_id = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
"""

USER_LIST = """
    SELECT user_id, nick_name FROM t_user_info
      WHERE nick_name LIKE %(nick_name)s
"""

GRP_USE = """
    SELECT EXTRACT(MINUTE FROM (last-creat)) AS grp_use FROM (
        SELECT COALESCE(last_time, '1990-01-01 00:00:00.00'::timestamp) AS last, COALESCE(create_time, '1990-01-01 00:00:00.00'::timestamp) AS creat
          FROM t_group_user
          WHERE user_id = %(user_id)s
            AND create_time >= %(start_time)s
            AND create_time < %(end_time)s
    ) AS group_use
"""

# GRP_USE = """
#     SELECT last_time, create_time FROM t_group_user
#       WHERE user_id = %(user_id)s
#         AND create_time >= %(start_time)s
#         AND create_time < %(end_time)s
# """

NUM_DEP_DOC = """
    SELECT COALESCE(COUNT(*), 0) AS num_dep_doc FROM t_article_contribute
      WHERE create_user = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
"""

NUM_DEP_COM = """
    SELECT COALESCE(SUM(num), 0) AS num_dep_com FROM (
      SELECT COUNT(*) AS num FROM t_comment_1 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_2 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_3 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_4 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_5 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_6 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_7 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_8 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_9 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
        UNION ALL
        SELECT COUNT(*) AS num FROM t_comment_10 WHERE create_user = %(user_id)s AND create_time >= %(start_time)s AND create_time < %(end_time)s
    ) AS department_comment
"""

NUM_DEP_TAG = """
    SELECT COALESCE(COUNT(*), 0) AS num_dep_tag FROM t_doc_tag
      WHERE create_user = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
"""

NUM_DEP_STAY = """
    SELECT COALESCE(SUM(stay_time), 0) AS num_dep_stay FROM (
        SELECT log.* FROM log_department_stay AS log
          INNER JOIN t_department AS dpt
            ON dpt.id::varchar = log.name
    ) AS department_stay
      WHERE user_id = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
"""

NUM_DEP_READ = """
    SELECT COALESCE(COUNT(*), 0) AS num_dep_read FROM (
        SELECT log.* FROM log_department_click AS log
          INNER JOIN t_department AS dpt
            ON dpt.id::varchar = log.name
    ) AS department_readed
      WHERE user_id = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s 
"""

ALL_STAY = """
    SELECT COALESCE(SUM(stay_time), 0) AS all_stay FROM log_department_stay
      WHERE user_id = %(user_id)s
        AND create_time >= %(start_time)s
        AND create_time < %(end_time)s
"""

# ALL_CONTRI = NUM_DEP_DOC


QUERY_STATEMENTS = [USER_NAME, NUM_DOC, NUM_REPLY, NUM_TAG, NUM_TAG_LIKE, NUM_DOC_LIKE, NUM_TAG_LIKED, 
    NUM_READ, NUM_STAY, NUM_PRIVATE, NUM_DEL, NUM_FRO, GRP_USE, NUM_DEP_DOC, NUM_DEP_COM, NUM_DEP_TAG,
    NUM_DEP_STAY, NUM_DEP_READ, ALL_STAY
]