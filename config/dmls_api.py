#coding:utf-8


# 用户模拟类型剧情的挑战评价（总分数，所有剧情分数的总和，每个剧情只同时存在一个分值，再次挑战覆盖上一次的分值）
USER_INFO = """
    SELECT b.challenger_id AS user_id, b.total_score AS total_score, a.name AS user_name, a.avatar AS avatar, a.get_coins AS get_coins
      FROM
        (SELECT challenger_id, SUM(highest_score) AS total_score FROM simulation_challenge
          GROUP BY challenger_id
          ORDER BY total_score DESC) as b
      JOIN user_info AS a on a.id = b.challenger_id
      WHERE b.challenger_id = %(challenger_id)s
"""

USER_INSERT = """
    INSERT INTO user_info(name, avatar, w_id)
      VALUES(%(user_name)s, %(avatar)s, %(w_id)s)
"""

# a list, 模拟类型剧情的排行榜
USER_RANK = """
    SELECT a.challenger_id AS user_id, a.highest_score AS highest_score, a.plot_id AS plot_id, b.plot_name AS plot_name, c.name AS user_name, c.avatar AS avatar 
      FROM simulation_challenge AS a
      JOIN user_info AS c ON a.challenger_id = c.id
      JOIN simulation_plot AS b ON a.plot_id = b.id
      LIMIT %(limit)s 
"""

COIN_UPDATE = """
    UPDATE user_info
      SET get_coins = %(coins)s
      WHERE id = %(user_id)s
"""

SIMULATION_PLOTS = """
    SELECT id, cover_path, plot_name, position FROM simulation_plot
      WHERE delete = 0 AND type_id = %(type_id)s
      ORDER BY position
"""

SIMULATION_PLOT = """
    SELECT id, cover_path, plot_name, position, plot_json FROM simulation_plot
      WHERE id = %(plot_id)s AND delete = 0
"""

CHAPTER_PLOTS = """
    SELECT id, plot_name, position FROM chapter_plot
      WHERE delete = 0 AND type_id = %(type_id)s
      ORDER BY position 
"""

CHAPTER_PLOT = """
    SELECT id, plot_name, position, plot_json FROM chapter_plot
      WHERE delete = 0 AND id = %(plot_id)s
"""


USERS = {
    "USER_RANK": USER_RANK,
    "USER_INFO": USER_INFO,
    "USER_INSERT": USER_INSERT,
    "COIN_UPDATE": COIN_UPDATE,
}

SIMULATIONS = {
    "SIMULATION_PLOTS": SIMULATION_PLOTS,
    "SIMULATION_PLOT": SIMULATION_PLOT,
}

CHAPTERS = {
    "CHAPTER_PLOTS": CHAPTER_PLOTS,
    "CHAPTER_PLOT": CHAPTER_PLOT,
}